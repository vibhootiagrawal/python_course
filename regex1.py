# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:49:16 2019

@author: Education
"""

import re

i = 1
li = []

N = int(input("enter"))

while(i <= N):
    n= input()
    li.append(n)
    i = i+1
for n in li:
  reg = re.match(r'^[+-.]?\d*\.\d+$',n)
  
  if reg:
      print("true")
      
  else:
      print("false")
  

