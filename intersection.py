# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:58:20 2019

@author: Education
"""

list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,15]
s3=[]
s3=list(set(list2).intersection(set(list1)))
print(s3)