from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import ClientMessage, SystemDetails
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return render(request, 'drivingschool_manager/index.html', {})


def privacy_policy(request):
    template = loader.get_template('drivingschool_manager/privacypolicy.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def imprint(request):
    template = loader.get_template('drivingschool_manager/imprint.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('drivingschool_manager/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required
def admin(request):
    try:
        system_details = SystemDetails.objects.all()[0]
    except (IndexError, SystemDetails.DoesNotExist):
        system_details = None

    client_message_list = None
    search_value = request.GET.get('search-value')
    search_by = request.GET.get('search-by')

    if search_by is None:
        search_by = "name"

    if search_value is None:
        search_value = ""

    if search_value == "" or search_value is None:
        client_message_list = ClientMessage.objects.all().order_by('-message_date')
    else:
        if search_by == "name":
            client_message_list = ClientMessage.objects.filter(
                name__icontains=search_value).order_by('-message_date')
        elif search_by == "phone":
            client_message_list = ClientMessage.objects.filter(
                telephone__icontains=search_value).order_by('-message_date')
        elif search_by == "email":
            client_message_list = ClientMessage.objects.filter(
                email__icontains=search_value).order_by('-message_date')

    # Show 25 contacts per page.
    paginator = Paginator(client_message_list, 25)

    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    clients_page = paginator.get_page(page_number)

    context = {
        'system_details': system_details,
        'clients_page': clients_page,
        'search': {'field': search_by, 'value': search_value},
    }
    return render(request, 'drivingschool_manager/admin.html', context)


def register(request):
    template = loader.get_template(
        'drivingschool_manager/client_register.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def change_system_details(request):
    try:
        system_details = SystemDetails.objects.all()[0]
        system_details.email = request.POST['systememail']
        system_details.password = request.POST['systempassword']
        system_details.save()
    except (IndexError, SystemDetails.DoesNotExist):
        SystemDetails.objects.create(
            email=request.POST['systememail'], password=request.POST['systempassword'])
    finally:
        return HttpResponseRedirect(reverse('manage'))


def register_client(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    telephone = request.POST['phone']
    ClientMessage.objects.create(name=name,
                                 email=email,
                                 message=message,
                                 telephone=telephone,
                                 is_replied_to=False,
                                 is_read=False)
    try:
        system_details = SystemDetails.objects.all()[0]
        send_mail(
            'Nachricht von ' + name,
            '',
            system_details.email,
            [system_details.email],
            html_message='Nachricht von: ' + name + '<br>E-mail: ' + email + '<br>Tel.: ' + telephone + '<br> Nachricht: <br>' + message,
            fail_silently=False,
            auth_user=system_details.email,
            auth_password=system_details.password,
        )
    finally:
        return HttpResponseRedirect(reverse('register_client_result'))


def register_client_result(request):
    return render(request, 'drivingschool_manager/register_client_result.html', {})


def team(request):
    return render(request, 'drivingschool_manager/team.html', {})


def faq(request):
    return render(request, 'drivingschool_manager/faq.html', {})


def fuehrerscheine(request):
    return render(request, 'drivingschool_manager/fuehrerscheine.html', {})


def kontakt(request):
    return render(request, 'drivingschool_manager/kontakt.html', {})
