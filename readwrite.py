# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:54:14 2019

@author: Education
"""
import csv

cv1 = open("new.csv",mode= 'w')
cv1_writer = csv.writer(cv1)

with open("zoo.csv",mode = 'r') as cv:
    csv_reader = csv.reader(cv)
    for char in csv_reader:
        cv1_writer.writerow(char)
        cv1.flush()
cv1.close()    
       
        
with open("new.csv",mode = 'r') as cv:
    csv_reader = csv.reader(cv)
    for char in csv_reader:
        print(char)