from django.shortcuts import render

from .models import category


def home(request):
    return render(request, 'pages/home.html', context={
        'nome': 'Luciano Clemente'
    })


def categories(request):
    form = category()
    return render(request, 'pages/categories.html', context={
        'form': form
    })


def sobre(request):
    return render(request, 'pages/sobre.html')


def monthYears(request):
    return render(request, 'pages/monthYears.html')


def fontpayers(request):
    return render(request, 'pages/fontpayers.html')

