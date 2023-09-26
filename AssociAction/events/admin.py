from django.contrib import admin

from .models import Event, EventAddress

# Register your models here.
admin.site.register(Event)
admin.site.register(EventAddress)