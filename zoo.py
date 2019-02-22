# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:26:43 2019

@author: Education
"""

def Read():
    try:
        with open("zoo.csv",'r') as file:
         print(file.readlines())
    except Exception as e:
        print(e)
           
def function():
 list1 = []
 list3 = []  
 try:
     file = open("zoo.csv",'r')
     for line in file:
         x=line.split(",")
         list1.append(x[0])    
     print(list((set(list1))))  
    
 except Exception as e:
      print(e) 

def water():
   try:
       from collections import OrdereDict
       dict1 = OrdereDict()
       file = open("zoo.csv",'r')
       for line in file:
         x=line.split(",")
         list1.append(x[0])   
         list2.append(x[1])  
       y = list((set(list1)))
       z = list((set(list1)))
    
         
       
       
    
    
    
    
    
    
    
    
def Water():
 from collections import OrderedDict   
 dict1 = OrderedDict()        
 try:
     file = open("zoo.csv",'r')
     for line in file:
         x = line.split(",")
         water = " ".join(x[-1])
         dict1[x[0]] = dict1.get(water, 0) + x[2]
 except Exception as e:
      print(e)       
  
        
    
        
        
        
        
        
        
            
              
    
    
        
        
        
                
            