# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:41:50 2019

@author: Education
"""
list2 = list(map(int,input().split())) 
def unlucky(list1):
   a = len(list1)
   sum1 = 0
   
   if(a==0):
       return 0
   else:
      for i in list2:    
        if(i>=13):
          continue
        else:
         sum1=sum1+i
      return sum1  
  
a = unlucky(list2)
print(a)   




