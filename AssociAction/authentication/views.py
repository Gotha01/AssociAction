import os

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from AssociAction.settings import MEDIA_ROOT
from . import forms as fms
from .models import Address, UserAddress, CustomUser

User = get_user_model()

class RegisterView(View):
    register_form_class = fms.RegistrationForm
    template_name = "authentication/register.html"

    def get(self, request):
        register_form = self.register_form_class()
        return render(request, self.template_name, {'register_form': register_form})
    
    def post(self, request):
        form = self.register_form_class(request.POST)
        message = ''
        if form.is_valid():
            try:
                user = form.save()
                if user is not None:
                    message = 'Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.'
                    request.session['registration_message'] = message
                    return redirect('login')
            except ValueError as e:
                if "This email is already in use" in str(e):
                    messages.error(request, 'Cet email est déjà enregistré.')
                else:
                    messages.error(request, "Un champ a mal été renseigné.")
        return render(request, self.template_name, {
            'register_form': form,
        })

class LoginPageView(View):
    login_form_class = fms.LoginForm
    template_name = "authentication/login.html"
    
    def get(self, request):
        login_form = self.login_form_class()
        message = ''
        registration_message = request.session.pop('registration_message', None)
        return render(request, self.template_name, {
            'login_form': login_form,
            'registration_message': registration_message,
        })

    def post(self, request):
        login_form = self.login_form_class(request.POST)
        message = ''

        if login_form.is_valid():
            try: 
                user = authenticate(
                    username = login_form.cleaned_data['username'],
                    password = login_form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    message = 'identifiants invalides'
            except Exception as e:
                message = e

        return render(request, 'authentication/login.html', {
            'login_form': self.login_form_class,
            'message': message,
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

    if request.method == 'POST':
        img_form = fms.UserImageUpdateForm(request.POST, request.FILES, instance=request.user)
        user = request.user

        if 'save_address_form' in request.POST:
            address_form = fms.AddressUpdateForm(request.POST)
            if address_form.is_valid():
                user_address = UserAddress.objects.filter(user=user).first()
                if user_address:
                    old_address = user.get_address()
                    existing_user_address = address_form.save()
                    user_address.address = existing_user_address
                    user_address.save()
                    old_address.delete()
                    messages.success(request, "Adresse modifiée avec succès")
                else:
                    new_address = address_form.save()
                    UserAddress.objects.create(user=user,address=new_address)
                    messages.success(request, "Adresse enregistrée avec succès")
                return redirect('profile')
            
        elif 'submit_image' in request.POST:
            if img_form.is_valid():
                img_form.save()
                messages.success(request, 'Image enrgistrée avec succès')
                return redirect('profile')
            
        elif "delete_image" in request.POST:
            user_profile = CustomUser.objects.get(username=request.user.username)
            image_field_file = user_profile.user_img
            if image_field_file:
                image_field_file.delete()
                user_profile.user_img = None
                user_profile.save()
                messages.success(request, "Image de profil supprimée avec succès.")
                return redirect('profile')
            
        elif 'save_user_form' in request.POST:
            user_form = fms.UserProfileUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Informations modifiées")
                return redirect('profile')
            
    return render(request, 'authentication/user_profile_update.html', {
        'user_form': user_form,
        'img_form': img_form,
        'address_form': address_form,
    })
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')