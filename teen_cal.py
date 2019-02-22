# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:25:52 2019

@author: Education
"""
teen_list=[13,14,17,18,19]
keys=input("> ").split(" ")
item=list(map(int,input("> ").split(" ")))
dic={}
dic=dict(zip(keys,item))
print(dic)
sum=0
for i in dic.values():
    if i in teen_list:
        continue
    else:
        sum=sum+i
print(sum)        