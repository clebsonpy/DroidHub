from django.contrib import admin
from .models import Profile, User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'cpf_cnpj', 'phone', 'address']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']
