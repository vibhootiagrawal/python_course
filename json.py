# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:10:20 2019

@author: Education
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=kota"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3


response = requests.get(url)

response.content      #to get the content

jsondata = response.json()

print(type(jsondata))

for key,value in jsondata.items():
    print(key,":",value)
    
    
for key in jsondata:
     print(key)    
    
    
print(jsondata["coord"]["lon"])

print(jsondata["coord"]["lat"])    

print(jsondata["weather"])

print(jsondata["wind"])

print(jsondata["sys"]["sunrise"])

print(jsondata["sys"]["sunset"])