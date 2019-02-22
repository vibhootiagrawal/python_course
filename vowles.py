# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:42:46 2019

@author: Education
"""


list1 = []

for item in state_list:
    str1 = ""
    for char in item:
        if char not in vowel_list:
            str1 = str1 + char
            print (str1)
    list1.append(str1)
    
print (list1)
            
    
