# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:24:18 2019

@author: Education
"""


import requests

url = "https://free.currencyconverterapi.com/api/v6/convert?q=USD_INR&compact=ultra&apiKey=825e974f36627bbd68e6"
    
    
response = requests.get(url)

jsondata = response.json()

print(jsondata['USD_INR'])