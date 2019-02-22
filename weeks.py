# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:01:32 2019

@author: Education
"""
days=("monday",'tuesday','wednesday','thursday','friday','saturday')
name_of_days=input("enter days").split(",")
for i in days:
    if i not in name_of_days:
        name_of_days.insert(days[i],i)
print(tuple(name_of_days))        



x=[]
days=("monday",'wednesday','thursday','saturday')
x=list(days)
x.insert(1,"tuesday")
x.insert(4,"friday")
print(tuple(x))
