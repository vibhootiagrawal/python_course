# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:50:31 2019

@author: Education
"""
import re

readfile =  open("D:/forskNotes/phnbook.txt","r") 

res = readfile.read()

resq = re.findall(r'j\w*\sneu',res)

print(resq)




"^ = check from starting of a string like in file it check the first word of line"