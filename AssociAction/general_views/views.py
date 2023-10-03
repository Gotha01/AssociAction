from django.shortcuts import render
from django.db.models import Q
from .forms import SearchForm
from association.models import Association, UserRoleAssociation

def home(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid() or form.cleaned_data.get('quoi') or form.cleaned_data.get('ou'):
            quoi = form.cleaned_data.get('quoi')
            ou = form.cleaned_data.get('ou')

            associations = Association.objects.all()

            if quoi:
                associations = associations.filter(
                    Q(associationname__icontains=quoi) | Q(associationsector__sector__sectorname__icontains=quoi)
                )

            elif ou:
                associations = Association.objects.filter(
                    associationaddress__address__postalcode__icontains=ou
                ) | Association.objects.filter(
                    associationaddress__address__cityname__icontains=ou
                )
            
            for association in associations:
                association.sector = association.get_sector()

            context = {'associations': associations}
            return render(request, 'association/association_list.html', context)
        else:
            associations = Association.objects.all()[:25]
            context = {'associations': associations}
            return render(request, 'association/association_list.html', context)
        
    context = {'form': form}
    return render(request, 'general_views/home.html', context)

def help_center(request):
    return render(request, "general_views/help.html")

def legals(request):
    return render(request, "general_views/legals.html")

def contact(request):
    role = False
    user_role = UserRoleAssociation.objects.filter(role=1, user=request.user)
    if user_role:
        role = True
    return render(request, "general_views/contact.html", {'role': role})