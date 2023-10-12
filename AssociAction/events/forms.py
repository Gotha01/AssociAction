from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'description']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', }),
        }


class EventFormUpdate(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'description']
        labels = {
            "event_name": "Nom de l'évènement",
            "date": "Date",
            "description": "Description",
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', }),
        }
