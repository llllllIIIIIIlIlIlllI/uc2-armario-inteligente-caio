from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/status/', views.status_api),
    path('api/status_nichos/', views.api_status_nichos, name= 'status_nichos'),
]