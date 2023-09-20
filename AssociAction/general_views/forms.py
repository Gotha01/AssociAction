from django import forms

class SearchForm(forms.Form):
    quoi = forms.CharField(max_length=100)
    ou = forms.CharField(max_length=100)
