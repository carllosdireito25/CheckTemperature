from django.shortcuts import render
from core.ApiWeatherConnection.api_connection import WeatherAPI
from core.models import WeatherRecords
from core.utils.convert_to_celsius import get_celsius_format


def index(request):
    return render(request, 'index.html')


def resultado(request):
    city=request.POST.get('cidade')
    temperature = WeatherAPI().get_city_temperature(city)
    weather = WeatherRecords(city=city,temperature=temperature).save()
    return render(request, 'resultado.html',{"cidade":city,"temperature":temperature})


def registros(request):
    city=request.POST.get('cidade')
    registros = WeatherRecords.objects.filter(city=city)
    return render(request, 'resultadoPesquisa.html',{"cidade":city,"registros":registros})