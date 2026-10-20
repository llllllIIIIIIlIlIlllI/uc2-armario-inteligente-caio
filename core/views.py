from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'titulo': 'Armário de Chaves do Senai',
        'Nome': 'Caio Paiva'
    }
    return render(request, 'index.html')
