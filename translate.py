# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:50:18 2019

@author: Education
"""


def translate(string):
    list1=[]
    vowel_list=["A","E","I","O","U","a","e","i","o","u"," "]
    for i in string:
        if i not in vowel_list:
            x=(i+"o"+i)
            list1.append(x)
        else:
            list1.append(i)
    for i in list1:
        print((i),end="")
s=input()    
translate(s)