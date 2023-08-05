from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser, Role, Address

class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'is_sex',
        'date_of_birth',
        'address',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    )
    list_filter = (
        'username', 'last_name', 'is_active', 'is_superuser', 'date_joined'
    )
    list_per_page = 25

class CustomAddressAdmin(UserAdmin):
    list_display = (
        'idaddress',
        'postalcode',
        'cityname',
        'addresslineone',
        'addresslinetwo',
    )
    list_filter = (
        'postalcode',
        'cityname',
    )
    list_per_page = 25

class CustomRoleAdmin(UserAdmin):
    list_display = (
        'idrole',
        'rolename',
        'rolepermission',
        'description',
    )
    list_filter = (
        'rolename',
        'rolepermission',
    )

admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Role)
