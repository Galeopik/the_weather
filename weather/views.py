import os
import requests

from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def index(request):
    weather_data = None
    error = None
    city = request.GET.get('city')
    if city:
        api_key = os.getenv('API_KEY', '')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=ru'
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                'city': city.title(),
                'temp': int(response['main']['temp']),
                'feels_like': response['main']['feels_like'],
                'description': response['weather'][0]['description'].title(),
                'wind': response['wind']['speed'],
                'clouds': response['clouds']['all'],
                'pressure': response['main']['pressure'],
                'icon': response['weather'][0]['icon'],
            }

        else:
            error = 'Город не найден. Проверьте название.'

    context = {
        'weather': weather_data,
        'error': error
    }

    return render(request, 'index.html', context)
