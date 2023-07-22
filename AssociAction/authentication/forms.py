from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    # Autres champs pour l'inscription