from django.contrib import admin

from .models import Event, EventAddress, AssociationEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(EventAddress)
admin.site.register(AssociationEvent)