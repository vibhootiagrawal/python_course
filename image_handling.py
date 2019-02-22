# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:30:38 2019

@author: Education
"""
size=(34,34)
#PIL stands for python imaging library to deal with images to open manipulate the images
from PIL import Image,ImageFilter

f=Image.open("IMG20171019190155.jPG")

original=f.filter(ImageFilter.EMBOSS)      #EMBOSS,BLUR,CONTOUR etc are the effects on image

original.save("MY.png")                   #save is used to save the images which takes one parameter
   
original.thumbnail(size)         #it reduce the size of image to the given size

original.save("My.png")

original.show()




