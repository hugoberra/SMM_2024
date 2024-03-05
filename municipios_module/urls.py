from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_municipio, name='registrar_municipio')
]