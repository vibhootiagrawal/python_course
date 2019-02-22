# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:26:40 2019

@author: Education
"""
import hashlib                            #used to import for cryptography


try:
 file = open("romeo.txt",'rt')

 for line in file:
   h = hashlib.sha1(line.encode())        #encode function is used to encode a string 
                                          #hashib is used to make a object of hashlib 
except Exception as e:
     print(e)                                          
                    
else:                      
     print(h.hexdigest())                     #hesxdigest function used to get the hash value in hexdecimal value
     #print(h.digest())                       #hash value in \ form

finally:
    file.close()


