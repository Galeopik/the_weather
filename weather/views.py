import os
import requests

from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def index(request):
    weather_data = None
    city = request.GET.get('city')
    if city:
        api_key = os.getenv('API_KEY', '')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=ru'
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                'city':city.title(),
                'temp':response['main']['temp'],
                'description':response['weather'][0]['description'].title(),
                'icon': response['weather'][0]['icon'],
            }

    return render(request, 'index.html', {'weather': weather_data})
