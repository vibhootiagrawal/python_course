# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:58:12 2019

@author: Education
"""
import numpy as n
a=n.array([[1,2,5],[4,3,1],[3,2,1]])
print(a.shape)
print(a[0,1])
print(a[0:2,2:3])



import numpy as np
a=np.zeros((2,3))
print(a)
b=np.ones((1,2))
print(b)
print(b[0:1,0:2])
c=np.eye((3))
print(c)
d=np.full((2,6),7,"D")
print(d[1:2,0:1])
print(d)
e=np.ones((4,3))
print(e)   


import numpy as np
a.shape=(3,2)   #used to reshape an array
print(a)
f=e.reshape((6,2))    #also used to reshape an array
print(f)

import numpy as np
a=[[1,2,3],[4,5,6],[1,6,3]]
print(a[1:2])