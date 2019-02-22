# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:51:31 2019

@author: Education
"""

from PIL import Image

img = Image.open("IMG20171019190155.jpg")



#print(img.mode)        to show the mode of image

img_gray = img.convert(mode = 'L')      #to convert the mode of a image
img_gray.show()                        #to show the image




img_rotate = img.rotate(90)
img_rotate.show()             #to rotate a iamge


#to crop a image 
img_crop = img.crop((40,80,100,204))
img_crop.show()


#to crop a image from center
new_width = 160
new_height = 204

width,height = img.size

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

img_crop1 = img.crop((left,top,right,bottom))
img_crop1.show()


save = img.copy()              #to create copy of image
save.show()


size = (56,45)
img.thumbnail(size)
img.show()