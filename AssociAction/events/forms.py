from django import forms
from .models import Event, EventAddress

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'description']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date',}),
        }

class EventAddressForm(forms.ModelForm):
    class Meta:
        model = EventAddress
        fields = ['address']