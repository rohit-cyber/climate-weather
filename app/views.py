from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
 

    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=b528298732d4abd84d74b5a8aba55a13'

    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()

    form=CityForm()

    cities=City.objects.all()

    weather_data=[]

    for city in cities:

        r=requests.get(url.format(city)).json()

        city_weather={
        'city':r['name'],
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }

        weather_data.append(city_weather)
    print(weather_data)
    context={'weather_data':weather_data,'form':form}

    return render(request,'weather.html',context)


