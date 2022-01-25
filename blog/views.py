from django.shortcuts import render

def musician_list(request):
    return render(request, 'blog/musician_list.html', {})
