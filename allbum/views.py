from django.shortcuts import render
from .models import Allbum


# Create your views here.

def allbum(request):
    allbum = Allbum.objects.all()
    context = {
        'allbum': allbum
    }

    return render(request, 'allbum/index.html', context)
