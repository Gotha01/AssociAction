from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser, Address, UserAddress


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password')}
        ),
        (
            'Personal Info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'username',
                    'phone_number',
                    'user_img',
                    'date_of_birth')
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_admin',
                    'is_active',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                    )
            }
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login', 'date_joined'
                )
            }
        ),
    )
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'date_of_birth',
        'is_active',
        'is_superuser',
        'date_joined',
    )
    list_filter = (
        'is_active',
        'is_superuser',
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)


class CustomAddressAdmin(UserAdmin):
    list_display = (
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)
admin.site.register(UserAddress)
