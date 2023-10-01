#! /usr/bin/env python3

from pyowm import OWM
import os 

# key for openweather
API_KEY = os.environ.get('API_KEY')

# OWM config
owm = OWM('ede00405f37a74c13f69a2a629abcc66')

#manager owm 
manager = owm.weather_manager()


def weater_function(place):
    """Return temp, wind, clouds"""

    weather_list = []
    observer = manager.weather_at_place(place)
    weather = observer.weather
    temp_data=weather.temperature('celsius')
    temp_data = temp_data['temp']
    wind = weather.wind()
    wind_data = wind['speed']
    clouds_data = weather.clouds
    weather_list.append(temp_data)
    weather_list.append(wind_data)
    weather_list.append(clouds_data)
    weather_list.append(place)
    return weather_list
