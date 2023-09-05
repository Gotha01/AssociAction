from django import forms
from .models import Association


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


class AskAssociationRights(forms.Form):
    content = forms.CharField(label='Contenu de la demande  :', widget=forms.Textarea)
    association_already_in_app = forms.BooleanField(
        label="Mon association est déjà dans l'application(Cochez la case si c'est le cas).",
        required=False
    )
    association_name = forms.CharField(
        label="Nom de mon association (si elle est déjà dans l'application)",
        required=False
    )