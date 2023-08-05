from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, Address

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    form_title = "Se connecter"
    

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    form_title = "Créer un compte"

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Le mot de passe doit comporter au moins 8 caractères.')
        if password.islower() or password.isupper():
            raise ValidationError('Le mot de passe doit comporter des caractères en majuscules et en minuscules.')
        return password
    
class UserProfileUpdateForm(forms.ModelForm):
    SEX_CHOICES = (
        (1, 'Masculin'),
        (2, 'Féminin'),
    )
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'date_of_birth',]
        labels = {
            'first_name': 'Prénom *',
            'last_name': 'Nom *',
            'username': 'Nom d\'utilisateur *',
            'email': 'Adresse e-mail *',
            'phone_number': 'Numéro de téléphone (0601020304)',
            'user_img': 'Image de profil',
            'date_of_birth': 'Date de naissance',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Utilisation du widget DateInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Définir les valeurs actuelles de l'utilisateur connecté comme valeurs initiales.
        """if self.instance:
            self.fields['email'].initial = self.instance.email
        else:
            self.field"""

class UserImageUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['user_img',]
        labels = {'user_img': 'Image de profil',}

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