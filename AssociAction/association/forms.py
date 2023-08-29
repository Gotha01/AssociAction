from django import forms
from .models import Association, AssociationAddress
from authentication.models import Address  # Assurez-vous d'importer le modèle Address correctement

class AssociationCreateForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ['associationname', 'acronym', 'phone_number', 'email', 'description', 'logo']
        labels = {
            'associationname': "Nom de l'association",
            'acronym': 'Acronyme',
            'phone_number': 'Numéro de téléphone',
            'email': 'Adresse e-mail',
            'description': 'Description',
            'logo': "Logo de l'association",
        }
