from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .utils import buscar_status_nichos_banco

# Create your views here.


def index(request):
    context = {
        'titulo': 'Armário de Chaves do Senai',
        'Nome': 'Caio Paiva'
    }
    return render(request, 'index.html', context)


def status_api(request):
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})


def api_status_nichos(request):
    nichos = buscar_status_nichos_banco()
    return JsonResponse(nichos, safe=False, status=200)