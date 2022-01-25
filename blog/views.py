from django.shortcuts import render
from .models import Musicians, Album, Band

def musician_list(request):
    musician=Musicians.objects.all()
    return render(request, 'blog/musician_list.html', {'musician':musician})
