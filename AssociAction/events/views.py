from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from functools import wraps

from .models import Event, AssociationEvent, EventAddress
from .forms import EventForm, EventFormUpdate
from authentication.forms import AddressUpdateForm
from association.models import Association, UserRoleAssociation, Role


def check_responsible_roles(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, association_id, *args, **kwargs):
            try:
                association = Association.objects.get(id=association_id)
                user_role = UserRoleAssociation.objects.get(
                    user=request.user,
                    association=association
                ).role
                if user_role.id in allowed_roles:
                    return view_func(request, association_id, *args, **kwargs)
                else:
                    return redirect('home')
            except ObjectDoesNotExist:
                return redirect('home')
        return _wrapped_view
    return decorator


@login_required
@check_responsible_roles([1, 2])
def create_event(request, association_id):
    association = Association.objects.get(id=association_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            AssociationEvent.objects.create(
                association=association,
                event=event
            )
            return redirect(
                'event_address',
                association_id=association_id,
                event_id=event.id
            )
    else:
        form = EventForm()

    context = {
        'form': form,
        'address_form': 'address_form',
        'association': association,
        }
    return render(request, 'events/create_event.html', context)


def association_events(request, association_id):
    association = Association.objects.get(id=association_id)
    association_events = AssociationEvent.objects.filter(
        association=association
    )
    association_events = association_events.order_by('event__date')
    return render(
        request,
        'events/association_events.html',
        {
            'association': association,
            'association_events': association_events,
        }
    )


def event_detail(request, association_id, event_id):
    association = Association.objects.get(id=association_id)
    event = Event.objects.get(id=event_id)
    try:
        address = EventAddress.objects.get(event=event).address
    except EventAddress.DoesNotExist:
        address = ""

    roles = (Role.objects.get(id=1), Role.objects.get(id=2))
    try:
        have_roles = UserRoleAssociation.objects.get(
            user=request.user,
            association=association
        )
        if have_roles.role in roles:
            user_resp = True
            return render(
                request,
                'events/event_detail.html',
                {
                    'event': event,
                    'association': association,
                    'address': address,
                    "user_resp": user_resp
                }
            )
    except UserRoleAssociation.DoesNotExist:
        user_resp = False
    if request.method == 'POST':
        if 'delete_event' in request.POST:
            event.delete()
            redirect('association_detail', association_id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
            'association': association,
            'address': address
        }
    )


@login_required
@check_responsible_roles([1, 2])
def event_update(request, association_id, event_id):
    association = Association.objects.get(id=association_id)
    event = Event.objects.get(id=event_id)
    event_form = EventFormUpdate(instance=event)

    if request.method == 'POST':
        event_form = EventFormUpdate(request.POST, instance=event)
        if event_form.is_valid():
            event = event_form.save()
            return redirect(
                'event_detail',
                association_id=association_id,
                event_id=event_id
            )

    context = {
        'form': event_form,
        'association': association,
    }
    return render(request, 'events/event_update.html', context)


@login_required
@check_responsible_roles([1, 2])
def event_delete(request, association_id, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('association_detail', association_id=association_id)


@login_required
@check_responsible_roles([1, 2])
def event_address(request, association_id, event_id):
    form = AddressUpdateForm()
    if request.method == 'POST':
        form = AddressUpdateForm(request.POST)
        if form.is_valid():
            new_address = form.save()
            actual_event = Event.objects.get(id=event_id)
            EventAddress.objects.create(
                event=actual_event,
                address=new_address
            )
            return redirect(
                'event_detail',
                association_id=association_id,
                event_id=event_id
            )
    return render(request, 'events/event_address_create.html', {'form': form})
