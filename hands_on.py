# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:17:43 2019

@author: Education
"""
Even_list=[]
odd_list=[]
list1=list(range(1,20))
for i in list1:
   odd_list=list1[::2]
   Even_list=list1[1:len(list1):2]
print(odd_list)
print(Even_list)
            
