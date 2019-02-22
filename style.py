# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:33:24 2019

@author: Education
"""
import math
Number=int(input("enter number"))
dir(math)
help(math.factorial)
math.factorial(Number)


import math
radius=int(input("enter radius"))
area=(math.pi)*radius*radius
perimiter=2*(math.pi)*radius
print(area,perimiter)



#implementation of string function

dir(str)
help(str.lower)
help(str.upper)
help(str.capitalize)
help(str.title)
string=input("enter name")
print(string.title())
print(string.lower())
print(string.upper())
x=string.capitalize()
print(x)