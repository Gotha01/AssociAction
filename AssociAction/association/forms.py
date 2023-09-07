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
            'sector': "Secteur associatif"

        }
        widgets = {
            'associationname': forms.TextInput(attrs={'style': ''}),
            'email': forms.EmailInput(attrs={'style': ''}),
            'acronym': forms.TextInput(attrs={'style': ''}),
            'phone_number': forms.TextInput(attrs={'style': ''}),
            'description': forms.TextInput(attrs={'style': ''}),
            'logo': forms.ClearableFileInput(attrs={'style': ''}),
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