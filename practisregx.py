# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:18:00 2019

@author: Education
"""

'vibhooti agrawal'
'vidhan Arora'
'piyush Kumar'

a = 'vibhooti.hnd@gmail.com'
b = 'vidhanarora19997@gmail.com'
c = 'pk62893@gmail.com'
import re
 
result = re.findall(r'\w+\@\w{5}\.\w{3}','vibhooti.hnd#gmail.com,vidhanarora19997@gmail.com,pk62893@gmail.com')
print(result)

sam = "The sky is really beautiful and so is the sea"

res = re.match(r"[tis]?\w+",sam)
print(res)
res.group()


import re

list = ["guru89 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
    if z:
      print(z.group(0))     #return complete one search im the case of multiple search
      print(z.group(1))     #return 1 grouping value in one search
      print(z.group(2))     #return 2 grouping value in second search
    
