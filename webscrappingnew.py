# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:37:17 2019

@author: Education
"""

import requests

from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

response = requests.get(url).text

soup = BeautifulSoup(response,'lxml')  

Head = soup.find("h1",class_="firstHeading")

print(Head.text)    

Para = soup.find_all("p")[1]

print(Para.text)    



list1 = soup.find("div",class_="toc")

print(list1.text)


required_ul = soup.find_all("ul")[3]

print(required_ul.text)