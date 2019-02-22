# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:30:38 2019

@author: Education
"""

list1=list(map(int,input().split()))
def centered(list2):
    sort_list=[]
    sort_list=sorted(list2)
    print(sort_list)
    sum1=0
    add=0
    a=len(list2)
    for i in sort_list[1:a-1]:
        sum1=sum1+i
    add=len(list2)-2
    mean_avg=0.0
    mean_avg=(sum1/add)
    return mean_avg
a=centered(list1)
print(a)
    


