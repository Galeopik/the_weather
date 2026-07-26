import requests

from django.shortcuts import render


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a026f6573c3305150058c0d39784dc07'
    city = "Moscow"
    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'index.html')
