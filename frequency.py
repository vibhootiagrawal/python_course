# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:57:53 2019

@author: Education
"""
dict1={}
str1=input("enter string")
for i in str1:
    x=str1.count(i)
    dict1[i]=x
print(dict1)    
    

#version 02

dict1={}
str1="Vibhooti Agarwal"
for i in str1:
    if i not in dict1.keys():
        dict1[i] = str1.count(i)
    
print(dict1)    
    



#version 03 more optimize way using advance python
from collections import Counter       #import collections

myStr = input("enter string: ")

frequency = Counter(myStr)            #collections.Counter
print(frequency)                      #return counter type

for key,value in (dict(frequency).items()):
    print(key,":",value)

