from django.contrib import admin
from .models import Association, Sector, UserRoleAssociation, AssociationSector, AssociationAddress, Role

# Register your models here.

class AssociationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'associationname',
        'acronym',
        'phone_number',
        'email',
        'description'
    )
    list_display_links = (
        'id',
        'associationname'
    )
    search_fields = (
        'associationname',
        'acronym',
        'phone_number',
        'email',
        'description'
    )
    list_per_page = 25

class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'sectorname',
        'description'
    )
    list_display_links = (
        'sectorname',
    )
    search_fields = (
        'sectorname',
    )
    list_per_page = 25

class UserRoleAssociationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'association',
        'role'
    )
    list_display_links = (
        'user',
        'association',
        'role'
    )
    list_filter = (
        'association',
        'role'
    )
    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__email',
        'association__associationname',
        'role__rolename'
    )
    list_per_page = 25

class AssociationSectorAdmin(admin.ModelAdmin):
    list_display = (
        'association',
        'sector'
    )
    list_display_links = (
        'association',
        'sector'
    )
    list_filter = (
        'association',
        'sector'
    )
    search_fields = (
        'association__associationname',
        'sector__sectorname'
    )
    list_per_page = 25

class AssociationAddressAdmin(admin.ModelAdmin):
    list_display = (
        'association',
        'address'
    )
    list_per_page = 25

admin.site.register(Association, AssociationAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(UserRoleAssociation, UserRoleAssociationAdmin)
admin.site.register(AssociationSector, AssociationSectorAdmin)
admin.site.register(AssociationAddress, AssociationAddressAdmin)
admin.site.register(Role)