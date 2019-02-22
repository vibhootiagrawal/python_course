# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:21:31 2019

@author: Education
"""

import re
N = int(input("enter")) 
i = 1
li = []
lsi = []

while(i <= N):
    n = input()
    li.append(n)
    i = i+1
    
#result = re.split(r'\@',number)   
#lsi.append(result[0])      
#lsi1.append(result[1])
#li = sorted(lsi)  

for mail in li:
   result = re.findall(r'\w+@\w+\.\w+',mail)
   lsi.extend(result)
   
print(sorted(lsi))   