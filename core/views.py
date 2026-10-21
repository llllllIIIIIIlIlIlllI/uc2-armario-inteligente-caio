from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    context = {
        'titulo': 'Armário de Chaves do Senai',
        'Nome': 'Caio Paiva'
    }
    return render(request, 'index.html', context)


def status_api(request):
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})