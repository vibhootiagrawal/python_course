# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:50:31 2019

@author: Education
"""

import requests

from bs4 import BeautifulSoup

wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

#access the data by url
response = requests.get(wiki).text  #access text data in unstructured format

soup = BeautifulSoup(response)    #convert the data in html structured format

div = soup.find("div",class_="global-header")   #access the div and the class global-header

print(div)                                    #print the data

main = soup.find_all("main",id="main-content")   #access the main with the id main content

print(main)

table = soup.find_all("table")      #access all the table

print(table)

required_table = soup.find("table", class_="table")     #access the required table

print(required_table)

A = []
B = []
C = []
D = []
E = []

for row in required_table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 5:       #access the data without header it find those td which has rhe td
      A.append(cells[0].text)      # append 1 td of all tr in list A in text format
      B.append(cells[1].text)      # append 2nd td of all tr in list B
      C.append(cells[2].text)      # append 3rd td of all tr in list C
      D.append(cells[3].text)      #append 4th td of all tr in list D
      E.append(cells[4].text)      #append 5th td of all tr in list E
      
#import pandas to convert list to data frame
import pandas as pd
df = pd.DataFrame(A,columns = ["Pos"])
df["Team"] = B
df["WeightdMatches"] = C
df["Points"] = D
df["Rating"] = E    
      
print(df) #print the DataFrame     