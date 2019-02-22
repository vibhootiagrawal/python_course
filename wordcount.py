# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:44:32 2019

@author: Education
"""
from collections import Counter

fileName = input("enter file name> ")

def line():
 try:
    with open (fileName,'rt') as file:
        lines = file.readlines()
        line = Counter(lines)
        for key,value in line.items():              #count occurance of each line in file
            print(key,":",value)
            
 except Exception as e:
   print(e)            
   
   
   
def charcater():   
 try:
      with open (fileName,'rt') as file:
        lines = file.read()
        for key,value in Counter(lines).items():              #count occurance of each character in file
            print(key,":",value) 
 except:
    pass            
   
def word():
  try:
      with open (fileName,'rt') as file:
        lines = file.read().replace("\n"," ").split(" ")
        for key,value in Counter(lines).items():              #count occurance of each word in file
            print(key,":",value)
  except:
    pass            
            
def specialCharacter():
    
  try:
      dict1 = {}
      count = 0
      special = ["@","#","$","%","&","*"]
      with open (fileName,'rt') as file:
        lines = file.readlines()
        for line in lines:
            if line in special:
                dict1[line] = count + 1
        print(dict1)
  except:
     pass                    
        
 
choice = print("Enter choice what u wnat to count char,word,line,specialchar: ")

if choice.upper() == "CHAR":
    charcater()
    
elif choice.upper() == "WORD":    
    word()

elif choice.upper() == "LINE":
    line()
    
elif choice.upper() == "SPECIALCHAR":
   specialCharacter()    
 
else:
   print("Not call any function ")    