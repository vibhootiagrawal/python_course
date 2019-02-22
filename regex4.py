# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:47:08 2019

@author: Education
"""


import re

i = 1

li = []

lis = []

N = int(input("enter num:"))

li.extend([input("Enter E-mail:")for i in range(1,N+1)])


for mail in li:
    res = re.findall(r'\w+@\w+\.\w+',mail)
    lis.extend(res)
    print(lis)
        
    