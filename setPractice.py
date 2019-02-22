# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:38:21 2019

@author: Education
"""

s1={1,2,6,4}
s1.add(6)
print(s1)
s2={56,34}
s2.update(s1)
print(s2)
s2.remove(34)
print(s2)
s1.discard(3)
print(s1)
s3={23,13,56,78,89,1}
s4={34,12,4,3,5,1}
s5={}
s2={3,4}
s3={8,6}
s4={6,1}
s5=s1.intersection(s2,s3,s4)       #return the element which will be the common in all
print(s5)
s5=s1.union(s2,s3)
print(s5)
s5=s5.symmetric_difference(s2)
print(s5)


