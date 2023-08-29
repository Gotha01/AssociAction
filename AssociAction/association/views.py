from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from authentication.forms import AddressUpdateForm
from .models import Association, AssociationAddress
from .forms import AssociationCreateForm 


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
        if form.is_valid():
            form.save()
            AssociationAddress.objects.create
            messages.success(request, "Association créée avec succès.")
    return render(request, 'association/association_create.html', {'form': form})

def association_detail(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    if request.method == 'POST':
        pass
    return render(request, 'association/association_detail.html', {'association': association})

def association_list(request):
    pass