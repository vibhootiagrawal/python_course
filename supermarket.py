# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:51:15 2019

@author: Education
"""
from collections import OrderedDict

new = []
dict1 = OrderedDict()      #orderdict maintain the order of a dictionary 

#whole process show how take multiple inputs and store that inputs
while True:
    inp = input("Enter Item and Price: ")
    if inp == "":
        break
    item_list = inp.split(" ")
    price = int(item_list[-1])
    item = " ".join(item_list[:-1])          #we use join to remove list from here
    dict1[item] = dict1.get(item, 0) + price      #return the value of the given key if key in dictionary

print (dict1)



#how to take 3 inputs

inp=input("name age and number: ")
list1=inp.split(" ")
Name=list1[0]
age=int(" ".join(list1[1:-1]))
number=int(list1[-1])
print(type(age))
print(type(number))

print(Name,age,number)