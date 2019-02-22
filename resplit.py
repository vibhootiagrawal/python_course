# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:18:51 2019

@author: Education
"""


import re

N = int(input("enter")) 

i = 1

li = []

while(i <= N):
    n = input()
    li.append(n)
    i = i+1

for number in li:
    result = re.match(r'\d+\.\d+',number)   
    if result:
        x = re.findall(r'^\d+',number)
        y = re.findall(r'\d+$',number) 
        print(x)
        print(y)
    else:
        print(number)    

#version 2
import re
N = int(input("enter")) 

i = 1

li = []

lsi = []

while(i <= N):
    n = input()
    li.append(n)
    i = i+1
    
for number in li:
    result = re.split(r'\.',number)   
    lsi = lsi + result
print(lsi)

