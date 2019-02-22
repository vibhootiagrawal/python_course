# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:45:24 2019

@author: Education
"""


list1=[343, 4, 78, 90]
for i in list1:
    i = str(i)
    if(i==i[::-1]):
        print("true")
    else:
        print("false")
  