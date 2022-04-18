from django.contrib import admin
from .models import ClientMessage, SystemDetails, LeistungsKategorie, Leistung, FAQ

admin.site.register(ClientMessage)
admin.site.register(SystemDetails)
admin.site.register(LeistungsKategorie)
admin.site.register(Leistung)
admin.site.register(FAQ)
