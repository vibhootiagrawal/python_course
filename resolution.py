# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:04:43 2019

@author: Education
"""

from PIL import Image
try:
 image = Image.open("Capture.PNG")

 width,height = image.size
 print("Resolution: ",width,"X",height)
 
except Exception as e:
     print(e)
     
else:
    image.close()

finally:
  pass     
     




#these are the some other function to get height,width ,format and info of image
x=image.height
print(x)


y=image.width
print(y)

z=image.format
print(z)

p = image.info
print(p)