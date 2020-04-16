from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e8a038486e11484605665001d81b4a85'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {
        'weather': weather
    }
    
    return render(request, 'weather/index.html', context) # return the index.html template
