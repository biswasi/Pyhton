# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:54:14 2024

@author: irabati
"""

import requests,json
import urllib
import time
import datetime
import calendar

APP_ID = 'Test W'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def get_weather_data():
    city_name = input("Enter city name : >>").strip()
    complete_url = base_url + "appid=" + APP_ID + "&q=" + city_name
    
    print( "get weather data from openweathermap")
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 401 :
        print("response is empty..")
    else :
        
     temp = data['main']['temp']
     pressure = data['main']['pressure']
     temp_min = data['main']['temp_min']
     temp_max = data['main']['temp_max']
     humidity = data['main']['humidity']
     wind_speed = data['wind']['speed']
     try:
        wind_gust = data['wind']['gust']
     except KeyError:
        wind_gust = None
     wind_deg = data['wind']['deg']
     clouds = data['clouds']['all']
     try:
        rain = data['rain']['3h']
     except KeyError:
        rain = None
     try:
        snow = data['snow']['3h']
     except KeyError:
        snow = None
     weather_id = data['weather'][0]['id']
     sunrise = data['sys']['sunrise']
     sunset = data['sys']['sunset']
    
     print("Temperature :",str(temp ))
     print("Temerature (max)" ,str(temp_max))
     print("Temperature (min)",str(temp_min))
     print("Sunrise :",str(sunrise))
     print("Sunset :" ,str(sunset))
     print("Humidity:" ,str(humidity))
     print("Cloud:" ,str(clouds))
     print("Wind Speed:" ,str(wind_speed))

     return [temp, pressure, temp_min, temp_max, humidity, wind_speed, wind_gust, wind_deg, clouds, rain, snow,
            weather_id, sunrise, sunset]


def main():
    data = get_weather_data()
    
if __name__ == '__main__':
    main()
