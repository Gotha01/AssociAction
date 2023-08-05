from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms as fms
from .models import Address

User = get_user_model()

class LoginPageView(View):
    login_form_class = fms.LoginForm
    registration_form_class = fms.RegistrationForm
    template_name = 'authentication/login_and_register.html'
    
    
    def get(self, request):
        message = ''
        login_form = self.login_form_class()
        registration_form = self.registration_form_class()
        return render(request, 'authentication/login_and_register.html', {
            'login_form': login_form,
            'registration_form': registration_form,
            'message': message,
        })

    def post(self, request):
        login_form = self.login_form_class(request.POST)
        registration_form = self.registration_form_class(request.POST)
        message = ''
        registration_success = False

        if 'login_submit' in request.POST and login_form.is_valid():
            user = authenticate(
                username = login_form.cleaned_data['username'],
                password = login_form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'identifiants invalides'

        elif 'register_submit' in request.POST and registration_form.is_valid():
            user_model = get_user_model()
            new_user = user_model.objects.create_user(
                username = registration_form.cleaned_data['username'],
                email = registration_form.cleaned_data['email'],
                password = registration_form.cleaned_data['password'],
                first_name = registration_form.cleaned_data['first_name'],
                last_name = registration_form.cleaned_data['last_name'],
            )
            registration_success = True

        return render(request, 'authentication/login_and_register.html', {
            'login_form': self.login_form_class,
            'registration_form': self.registration_form_class,
            'message': message,
            'registration_success': registration_success,
        })

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'authentication/user_profile.html', {'user': user})

@login_required
def update_profile_view(request):
    user_form = fms.UserProfileUpdateForm(instance=request.user)
    img_form = fms.UserImageUpdateForm(request.FILES, instance=request.user)
    address_form = fms.AddressUpdateForm()
    # Recover user address
    address_instance = request.user.get_address()

    if request.method == 'POST':
        
        img_form = fms.UserImageUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if 'save_user_form' in request.POST:
            user_form = fms.UserProfileUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Informations générales mises à jour avec succès.")
                return redirect('update_profile')
            
        if img_form.is_valid():
            img_form.save()
            return redirect('update_profile')

        if 'save_address_form' in request.POST:
            address_form = fms.AddressUpdateForm(request.POST)
            if address_form.is_valid():
                
                postalcode = address_form.cleaned_data.get('postalcode')
                cityname = address_form.cleaned_data.get('cityname')
                addresslineone = address_form.cleaned_data.get('addresslineone')
                addresslinetwo = address_form.cleaned_data.get('addresslinetwo')
                # Update address if available
                if address_instance:
                    # Update non-empty fields of existing address
                    if postalcode:
                        address_instance.postalcode = postalcode
                    if cityname:
                        address_instance.cityname = cityname
                    if addresslineone:
                        address_instance.addresslineone = addresslineone
                    if addresslinetwo:
                        address_instance.addresslinetwo = addresslinetwo
                # Create a new address if it doesn't exist
                else:
                    if postalcode and cityname and addresslineone:
                        address_instance = Address.objects.create(
                            user=request.user,
                            postalcode=postalcode,
                            cityname=cityname,
                            addresslineone=addresslineone,
                            addresslinetwo=addresslinetwo,
            )
                messages.success(request, "Votre profil a été mis à jour avec succès.")

            return redirect('update_profile')

    return render(request, 'authentication/user_profile_update.html', {
        'user_form': user_form,
        'img_form': img_form,
        'address_form': address_form,
        'address_instance':address_instance
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')