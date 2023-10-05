from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from events.models import AssociationEvent, EventAddress
from authentication.forms import AddressUpdateForm
from .models import Association, Sector, AssociationAddress, AssociationSector, UserRoleAssociation
from .forms import AssociationCreateForm, AssociationUpdateForm, AssociationImageUpdateForm


def superuser_check(user):
    return user.is_superuser

@user_passes_test(superuser_check)
def create_association(request):
    if request.method == 'POST':
        form = AssociationCreateForm(request.POST, request.FILES)
        if form.is_valid():
            association = form.save()
            sector_id = request.POST.get('sector')
            if sector_id:
                sector = Sector.objects.get(pk=sector_id)
                AssociationSector.objects.create(association=association,sector=sector)
            messages.success(request, "Association créée avec succès.")
            return redirect('association_address', association_id=association.id)
    else:
        form = AssociationCreateForm()
    return render(request, 'association/association_create.html', {'form': form})

@user_passes_test(superuser_check)
def association_address(request, association_id):
    form = AddressUpdateForm()
    if request.method == 'POST':
        form = AddressUpdateForm(request.POST)
        if form.is_valid():
            new_address = form.save()
            actual_association = Association.objects.get(id=association_id)
            AssociationAddress.objects.create(association=actual_association, address=new_address)
            messages.success(request, "Adresse créée avec succès.")
            return redirect('association_detail', association_id = association_id)
    return render(request, 'association/association_address_create.html', {'form': form})

@login_required
def update_association(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    association_form = AssociationUpdateForm(instance=association)
    img_form = AssociationImageUpdateForm(request.FILES, instance=association)

    if request.method == 'POST':
        association_form = AssociationUpdateForm(request.POST, instance=association)
        img_form = AssociationImageUpdateForm(request.POST, request.FILES, instance=association)
        
        if association_form.is_valid():
            association_form.save()
            return redirect('association_detail', association_id=association.id)
        
        if 'submit_logo' in request.POST:
            if img_form.is_valid():
                img_form.save()
                return redirect('association_detail', association_id=association.id)
            
        elif "delete_logo" in request.POST:
            association = Association.objects.get(id=association_id)
            image_field_file = association.logo
            if image_field_file:
                image_field_file.delete()
                association.logo = None
                association.save()
                messages.success(request, "Image de profil supprimée avec succès.")
                return redirect('association_detail', association_id=association.id)

    context = {
            'association': association,
            'association_form': association_form,
            'img_form':img_form,
        }
    return render(request, 'association/association_update.html', context)

def association_detail(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    director, admin, member = False, False, False
    if request.user.is_authenticated:
        user_role_association = UserRoleAssociation.objects.filter(
            association=association,
            user=request.user
        ).first()

        if user_role_association:
            role = user_role_association.role.rolename
            if role == "Director":
                director = True
            elif role == "Admin":
                admin = True
            elif role == "Member":
                member = True

    try:
        next_asso_event = AssociationEvent.objects.filter(association=association).latest('id')
        next_event = next_asso_event.event
        try:
            next_event_address = EventAddress.objects.get(event=next_event).address
        except EventAddress.DoesNotExist:
            next_event_address=''
    except AssociationEvent.DoesNotExist:
        next_event = None
        next_event_address=''
    return render(
        request,
        'association/association_detail.html',
        {
            'association':association,
            'next_event':next_event,
            'address':next_event_address,
            'director':director,
            'admin':admin,
            'member':member,
        }
    )

def association_list(request, context):
    associations = context.get('associations', [])
    return render(request, "association/association_list.html", {'associations': associations})