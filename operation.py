# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:34:23 2019

@author: Education
"""

user_list=list(map(int,input().split()))
def Add(list1):
   add=0
   for i in list1:
       add=add+i
   print(add) 
     
def multiply(list1):
    mul=1
    for i in list1:
        mul=mul*i
    print(mul)
def largest(list1):
       temp=0
      maxi=list1[0]
      a=len(list1)
        for i in list1[2:a+1]:
            if(maxi >= list1[i-1]):
               maxi=list1[0]
           else:
             temp=maxi
             maxi=list1[i]
          
  print(maxi)     
             
def smallest(list1):
        temp=0
        mini=list1[0]
        a=len(list1)
        for i in list1[2:a+1]:
           if(mini<=list1[i-1]):
              mini=list1[0]  
           else:
                temp=mini
                mini=list1[i]
                
        print(mini)  
def sorting(list1):
    a=sorted(list1) 
    return a
def remove_duplicate(list1):
    a=len(list1)
    for i in list1[2:a+1]:
        if(list1[i-2]==list1[i-1]):
          list1.remove(i-2)
        else:
            pass
    print(list1)  
def New(list1):

  # Add(list1)
  # multiply(list1)
  # largset(list1)
  # smallest(list1)
  # b=sorting(list1) 
  # print(b) 
   remove_duplicate(list1)          


New(user_list)

dir(list)
             