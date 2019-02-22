# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 18:32:53 2019

@author: Education
"""
#format2.py
string=input("enter string")
print(string.replace(" ","*"))


#format3.py
string=input("enter string")
print('*'.join(string))



#format4.py
string=input("enter string :")
x=string.split(" ")
print(x[1]+" "+x[0])
    

#stringt.py
string=input("enter name :")
x=string.index(" ")
print(string[x:]+" "+string[0:x+1])


#restart.py
string="RESTART"
string = string.replace("R","$")
string =string.replace("$","R",1)
print(string)

