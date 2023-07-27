from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html', context={
        'nome': 'Luciano Clemente'
    })


def contato(request):
    return render(request, 'pages/contato.html')


def sobre(request):
    return render(request, 'pages/sobre.html')
