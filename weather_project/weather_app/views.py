from django.shortcuts import render
import requests
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        try:
            city = request.POST.get('city')
            if city is not None:
                link = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=yourAppIdKey'
                link_icon = "https://openweathermap.org/img/wn/{}@2x.png"
                weather_data = requests.get(link.format(city)).json()
                
                data = { 
                    "country_code": str(weather_data['sys']['country']), 
                    "coordinate": str(weather_data['coord']['lon']) + ' '
                                + str(weather_data['coord']['lat']),
                    "weather": str(weather_data['weather'][0]['description']),
                    "icon" : str(weather_data['weather'][0]['icon']), 
                    "temp": str(weather_data['main']['temp']),
                    "feels_like": str(weather_data['main']['feels_like']),
                    "min_temp": str(weather_data['main']['temp_min']),
                    "max_temp": str(weather_data['main']['temp_max']),
                    "visibility": str(weather_data['visibility']),
                    "city": str(weather_data['name']),
                    "pressure": str(weather_data['main']['pressure']), 
                    "humidity": str(weather_data['main']['humidity']), 
                    "icon_link": str(link_icon.format(weather_data['weather'][0]['icon'])),
                }
                
                return render(request,'index.html',data)
                
        except Exception as e:
            return render(request,'index.html')
    
    else    :
        data = {}
    return render(request,'index.html',data)
