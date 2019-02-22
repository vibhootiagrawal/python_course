# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:43:37 2019

@author: Education
"""
try:
  fileName = input("enter file name> ")

  file = open(fileName,'r')                         # to read complete file
  last = [line for line in file]


except Exception as e:
    print(e)
    
else:
    print(last)

finally:
   file.close()     
   
   
   
try:   
    fileName = input("enter file name> ")

    file = open(fileName,'r') 
    for line in file:
        pass
    print(file)          #print the details of file related to generation

except Exception as e:
    print("exception :",e)
    
else:
   print(line)    
   
finally:
    file.close()