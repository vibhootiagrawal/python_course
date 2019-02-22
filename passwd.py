# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:48:39 2019

@author: Education
"""
new = []
uniList = []
with open("D:/forskNotes/passwd",'r') as file:
   x = file.readlines()
   for i in x:
       print(i.split(":*"))
       uniList.append(i.split(":*")[0])
       
'''       
p = sorted(uniList)
for char in p:                #to sort complete each charcter
    x = sorted(char)
    for i in x:
        new.extend(x)
        print(sorted(new))
''''

for char in uniList:              #to sort complete each username sperately 
    print(sorted(char))
         