"""
Created on Thu Jul  4 02:54:14 2024
@author: irabati B
"""

#Q1: Create a python script called googlesearch that provides a command line utility to
 #perform google search. It gives you the top links (search results) of whatever you want to search Google

from googlesearch import search  
print("Enter what you want to search in Google: :") 
#query = "Python Script"
query = input(">> ").strip()  
  
for item in search(query, tld = "co.in", num = 12 , stop = 20, pause = 4):  
    print(item)  

# Q2: Create a script called location that return the location parameters of any location you want
# importing geopy library

from geopy.geocoders import Nominatim

loc =Nominatim(user_agent="ProjectCertification")
# entering the location name

print("Enter the address you want lat and lon :")
client_address = input(">> ").strip()
getLoc = loc.geocode(client_address)
 
# printing address
print(getLoc.address)
 
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
print(getLoc.raw)

#3 Create a script called weather that return the environmental parameters (temperature (min, max), windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you want; after passing arguments (like user api and city id)

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



