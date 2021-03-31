from django.urls import path

from .views import index, resultado, registros

urlpatterns = [
    path('', index, name='index'),
    path('resultado', resultado, name='resultado'),
    path('registros', registros, name='registros')
]