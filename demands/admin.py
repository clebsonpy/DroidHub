from django.contrib import admin
from .models import Address, Demands


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['cep', 'city', 'state', 'country']
    search_fields = ['cep', 'city', 'state']


@admin.register(Demands)
class DemandsAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'status', 'date_open', 'date_finish', 'status_tag']
    search_fields = ['address__cep', 'status']
