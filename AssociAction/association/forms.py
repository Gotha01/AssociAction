from django import forms
from .models import Association, Sector


class AssociationCreateForm(forms.ModelForm):
    sector = forms.ModelChoiceField(
        queryset=Sector.objects.all(),
        widget=forms.Select(attrs={'style': ''})
    )
    class Meta:
        model = Association
        fields = ['associationname', 'sector', 'email', 'acronym', 'phone_number', 'description', 'logo']
        labels = {
            'associationname': "Nom de l'association",
            'acronym': 'Acronyme',
            'phone_number': 'Numéro de téléphone',
            'email': 'Adresse e-mail',
            'description': 'Description',
            'logo': "Logo de l'association",
            'siret_number':"Numéro de SIRET",
            'sector': "Secteur associatif",

        }
        widgets = {
            'associationname': forms.TextInput(attrs={'required': 'required'}),
            'email': forms.EmailInput(attrs={'required': 'required'}),
            'acronym': forms.TextInput(attrs={'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'required': 'required'}),
            'description': forms.TextInput(attrs={'required': 'required'}),
            'logo': forms.ClearableFileInput(attrs={'required': 'required'}),
        }

class AssociationUpdateForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ['associationname', 'email', 'acronym', 'phone_number', 'description', 'siret_number']
        labels = {
            'associationname': "Nom de l'association",
            'acronym': 'Acronyme',
            'phone_number': 'Numéro de téléphone',
            'email': 'Adresse e-mail',
            'description': 'Description',
            'siret_number': "Numéro de SIRET",
        }
        widgets = {
            'associationname': forms.TextInput(),
            'email': forms.EmailInput(),
            'acronym': forms.TextInput(),
            'phone_number': forms.TextInput(),
            'description': forms.TextInput(),
        }

class AssociationImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ['logo',]
        labels = {'logo': 'logo',}