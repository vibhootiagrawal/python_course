# -*- coding: utf-8\\ -*-
"""
Created on Wed Jan  9 21:32:37 2019

@author: Education
"""

n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print('\n') 
for i in range(n-1,0,-1):    
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\n")    