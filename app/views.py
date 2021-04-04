from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def index(request):
 

    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=b528298732d4abd84d74b5a8aba55a13'
    city='pune'

    r=requests.get(url.format(city)).json()

    city_weather={
        'city':r['name'],
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
    }

    context={'city_weather':city_weather}

    return render(request,'weather.html',context)


