from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import CustomUser, Address


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Mot de passe'
    )
    form_title = "Se connecter"


class RegistrationForm(forms.Form):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\-]+$',
        message="Pour les noms et prénoms, "
        "entrez des lettres, seul '-' est toléré."
    )
    last_name = forms.CharField(
        max_length=50,
        label="Nom",
        validators=[name_validator]
    )
    first_name = forms.CharField(
        max_length=50,
        label="Prénom",
        validators=[name_validator]
    )
    username = forms.CharField(
        max_length=50,
        label="Nom d'utilisateur"
    )
    email = forms.EmailField(
        max_length=100,
        label="Adresse e-mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Mot de passe"
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmer le mot de passe"
    )
    form_title = "Créer un compte"

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if (password
            and password_confirmation
                and password != password_confirmation):
            raise ValidationError("Les mots de passe ne correspondent pas.")

        if len(password) < 8:
            raise ValidationError(
                'Le mot de passe doit comporter au moins 8 caractères.'
            )

        if password.islower() or password.isupper():
            raise ValidationError(
                'Le mot de passe doit comporter des caractères en majuscules'
                ' et en minuscules.'
            )

        return cleaned_data

    def save(self):
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = CustomUser.objects.create_user(
            last_name=last_name,
            first_name=first_name,
            username=username,
            email=email,
            password=password
        )

        return user


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'date_of_birth'
        ]
        labels = {
            'first_name': 'Prénom *',
            'last_name': 'Nom *',
            'username': 'Nom d\'utilisateur *',
            'email': 'Adresse e-mail *',
            'phone_number': 'Numéro de téléphone',
            'user_img': 'Image de profil',
            'date_of_birth': 'Date de naissance',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    save_user_form = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput,
        initial='save_user_form',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserImageUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['user_img']
        labels = {'user_img': 'Image de profil'}


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['postalcode', 'cityname', 'addresslineone', 'addresslinetwo']
        labels = {
            'postalcode': 'Code postal *',
            'cityname': 'Ville *',
            'addresslineone': 'Adresse (ligne 1) *',
            'addresslinetwo': 'Adresse (ligne 2)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
