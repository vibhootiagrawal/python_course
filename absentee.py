# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:02:09 2019

@author: Education
"""
st_list = []
while True:
    St_name = input("> ")
    #if St_name =="":
    #   break
    if len(st_list) <= 25:
      st_list.append(St_name)  
    else:
        break
try:
    file = open("Student1.txt","wt") 
    file.writelines(st_list)
except Exception as e:
   print("EXception:",e)
else:
    file = open("Student1.txt","rt") 
    print(file.read())
finally:
        file.close()