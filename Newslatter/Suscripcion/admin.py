from django.contrib import admin
from django.apps import AppConfig
from.models import Email

class EmailAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Email, EmailAdmin)

class ContactoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Suscripcion"