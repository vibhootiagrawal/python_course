# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:20:25 2019

@author: Education
"""


#both those method are used to identify a string and digit

#method1
dict1={}
c=0
D=0
str1=input("enter string")
for i in str1:
    if i.isdigit():
        D=D+1
    elif i.isalpha():
        c=c+1
    else:
        pass
 
dict1.update({"Character":c,"Digit":D})   
print(dict1)    


#method2
c=0
d=0
item=input("> ")
item1=item.lower()
for i in item1:
    if ('a' <= i <= "z"):
        c=c+1
    elif('0' <= i <= '9'):
        d=d+1
    else:
        pass   
dict1={}
dict1.update({"character":c,"digit":d})      
print(dict1)    