from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

from events.models import Event, AssociationEvent
from authentication.forms import AddressUpdateForm
from .models import Association, Sector, AssociationAddress, AssociationSector
from .forms import AssociationCreateForm, AssociationUpdateForm, AskAssociationRights
from decouple import config


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
            actual_asociation = Association.objects.get(id=association_id)
            AssociationAddress.objects.create(association=actual_asociation, address=new_address)
            messages.success(request, "Adresse créée avec succès.")
            return redirect('association_detail', association_id = association_id)
    return render(request, 'association/association_address_create.html', {'form': form})

@login_required
def update_association(request, association_id):
    if request.method == 'POST':
        form = AssociationUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            association = form.save()
            sector_id = request.POST.get('sector')
            messages.success(request, "Association mise à jour avec succès.")
            return redirect('association_address', association_id=association.id)
    else:
        form = AssociationCreateForm()
    return render(request, 'association/association_update.html', {'form': form})


def association_detail(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    try:
        next_asso_event = AssociationEvent.objects.filter(association=association).latest('id')
        next_event=next_asso_event.event
        return render(
            request,
            'association/association_detail.html',
            {'association':association, 'next_event':next_event}
        )
    except AssociationEvent.DoesNotExist:
        next_event = None
        return render(
            request,
            'association/association_detail.html',
            {'association' : association, 'next_event':next_event}
        )

    
@login_required
def request_dir_rights_view(request):
    if request.method == 'POST':
        form = AskAssociationRights(request.POST)
        if form.is_valid():
            subject = "Demande d'autorisation sur une application."
            contenu = form.cleaned_data['contenu']
            association_already_in_application = form.cleaned_data['association_deja_dans_application']
            nom_association = form.cleaned_data['nom_association']
            destinataire = config('admin_mail')
            
            if association_already_in_application:
                # Specific treatment if the association is already in the application
                if nom_association:
                    contenu += f"\nNom de l'association : {nom_association}"
                
            # send e-mail
            send_mail(
                subject,
                contenu,
                'votre_email@example.com',
                [destinataire],
                fail_silently=False,
            )
            
            return redirect('page_confirmation')
            
    else:
        form = AskAssociationRights()
    
    return render(request, 'association/rights_request.html', {'form': form})

def association_list(request, context):
    associations = context.get('associations', [])
    return render(request, "association/association_list.html", {'associations': associations})