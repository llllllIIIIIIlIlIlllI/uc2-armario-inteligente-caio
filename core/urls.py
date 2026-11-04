
from django.urls import path
from django.contrib import admin
from . import views
from core.api import api

urlpatterns = [
    path('', views.index, name='home'),
    path('api/status/', views.status_api),
    path('api/status_nichos/', views.api_status_nichos, name='status_nichos'),
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
