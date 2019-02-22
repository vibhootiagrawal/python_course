# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:33:03 2019

@author: Education
"""

from collections import Counter
file = open("romeo.txt",'r')
words=file.readlines()       # to read each character in a line how manytimes occur
for word in words:
    frequency = Counter(word)  
    for key,value in frequency.items():
        print(key,":",value,end="\n")
    
    
    
    
    
file = open("romeo.txt",'r')     #to read how many time each character in a file
words=file.read()       
frequency = Counter(words)  
print(frequency)
    



file = open("romeo.txt",'r')      #to read how many time a word occur in file
words=(file.read()).replace("\n"," ").split(" ")
frequency = Counter(words)
for key,value in frequency.items():
        print(key,":",value,end="\n")
            