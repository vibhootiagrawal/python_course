# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:11:11 2019

@author: Education
"""

import requests

from bs4 import BeautifulSoup

wiki =  "https://en.wikipedia.org/wiki/Democracy"

url = requests.get(wiki).text
soup = BeautifulSoup(url)

print(soup.prettify())


print (soup.head)          #it give the complete head content

print (soup.body) 

print (soup.body.div)     #it give div content of body

print (soup.body.div.p)

print(soup.find_all("div"))


div = soup.find("div",class_="mw-body")       #it return first occurance of div

print(div)

div = soup.find_all("div",class_="mw-body")  #it return all the occurance of div

print(div)

div = soup.find_all("div",class_="noprint")  #it return all the occurance of div whose class is noprint

print(div)