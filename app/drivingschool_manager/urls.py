from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datenschutzerklaerung/', views.privacy_policy, name='privacy'),
    path('impressum/', views.imprint, name='imprint'),
    path('manage/', views.admin, name='manage'),
    path('registrieren/', views.register, name='client_register'),
    path('change-system-details/', views.change_system_details, name='change_system_details'),
    path('register-client/', views.register_client, name='register_client'),
    path('register-client-result/', views.register_client_result, name='register_client_result'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('fuehrerscheine/', views.fuehrerscheine, name='fuehrerscheine'),
    path('kontakt/', views.kontakt, name='kontakt'),
]
