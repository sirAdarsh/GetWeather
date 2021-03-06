import urllib.request
import json
from django.shortcuts import render
from . import config



def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        try:
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=' + config.api_key).read()
            list_of_data = json.loads(source)
            data = {
                "city_name":str(city).upper,
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            print(data)
        except:
            if city == '':
                data = {
                    "error": str('City cant be empty')
                }
            else :
                data = {
                    "error": str('No such city found')
                }
    else:
        data = {}

    return render(request, "main/index.html", data)
    
