from django.shortcuts import render, get_object_or_404
from .models import Association

def association_detail(request, association_id):
    association = get_object_or_404(Association, id=association_id)
    return render(request, 'association/association_detail.html', {'association': association})

def association_list(request):
    pass