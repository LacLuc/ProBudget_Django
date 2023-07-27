from django.shortcuts import render


def home(request):
    return render(request, 'home.html', context={
        'nome': 'Luciano Clemente'
    })


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')
