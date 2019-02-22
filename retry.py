# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:52:32 2019

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
    resq = re.findall(r'\w+@\w+\.\w{2,4}',number)
    for i in resq:
        result = re.match(r'^\w+',resq) 
        print(result)