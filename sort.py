# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:52:25 2019

@author: Education
"""

my_str = "Hello this Is an Example With cased letters"

words = my_str.split()

words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)