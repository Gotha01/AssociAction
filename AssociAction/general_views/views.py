from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from search.forms import SearchForm

def home(request):
    form = SearchForm()
    context = {'form': form}
    return render(request, "general_views/home.html", context)

def help_center(request):
    pass