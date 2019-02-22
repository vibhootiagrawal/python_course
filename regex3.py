# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:33:03 2019

@author: Education
"""

import re

inp = input("enter number:")

res = re.findall(r'^[456]\d{3}\.?\d{4}\.?\d{4}\.?\d{4}',inp)

if res:
    print("valid")
    
else:
  print("invalid")    