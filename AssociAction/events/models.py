from django.db import models
from association.models import Association
from authentication.models import Address

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=400)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

class EventAddress(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)