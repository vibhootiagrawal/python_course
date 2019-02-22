# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:25:49 2019

@author: Education
"""

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]


order_Summary = list(map(lambda x : (x[2]*x[3],x[0]),orders))
  
invoice =list( map(lambda x : x if x[0] >= 100 else(x[0]+10,x[1]),order_Summary))
  

print(invoice)