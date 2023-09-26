from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from .models import Event, AssociationEvent
from .forms import EventForm
from association.models import Association

def staff_check(user):
    return user.is_staff

@user_passes_test(staff_check)
def create_event(request, association_id):
    association = Association.objects.get(id=association_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            AssociationEvent.objects.create(association=association,event=event)
            return redirect('association_detail', association_id=association_id)
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form, 'association': association})

def association_events(request, association_id):
    association_events = Event.objects.filter(associations=association_id)
    return render(request, 'events/association_events.html', {'association_events': association_events})

def event_detail(request, association_id, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})