from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

from authentication.forms import AddressUpdateForm
from .models import Association, AssociationAddress
from .forms import AssociationCreateForm, AskAssociationRights
from dev_config import admin_mail


def staff_check(user):
    return user.is_staff

@user_passes_test(staff_check)
def create_association(request):
    if not request.user.is_staff:
        messages.error(request, "Vous n'avez pas l'autorisation de créer une association.")
        return redirect('home')
    if request.method == 'POST':
        form = AssociationCreateForm(request.POST, request.FILES)
        if form.is_valid():
            association = form.save()
            messages.success(request, "Association créée avec succès.")
            return redirect('association_address', association_id=association.id)
    else:
        form = AssociationCreateForm()
    return render(request, 'association/association_create.html', {'form': form})

@user_passes_test(staff_check)
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

def association_detail(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    if request.user != None:
        if request.method == 'POST':
            pass
    return render(request, 'association/association_detail.html', {'association': association})

@login_required
def request_rights_view(request):
    if request.method == 'POST':
        form = AskAssociationRights(request.POST)
        if form.is_valid():
            subject = "Demande d'autorisation sur une application."
            contenu = form.cleaned_data['contenu']
            association_already_in_application = form.cleaned_data['association_deja_dans_application']
            nom_association = form.cleaned_data['nom_association']
            destinataire = admin_mail
            
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

def association_list(request):
    associations = Association.objects.all()
    return render(request, "association/association_list.html", {'associations':associations})