# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:10:06 2019

@author: Education
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Hindaun"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3

response = requests.get(url)

jsondata = response.json()

#print(jsondata)     used to print the complete jsondata

print(jsondata['corrd'])       #infomation about longitude and latitude


print(jsondata['weather'])    #information about weather condition


print(jsondata['wind']['speed'])    #infomaon about windspeed


print(jsondata['sys']['sunrise'])


print(jsondata['sys']['sunset'])