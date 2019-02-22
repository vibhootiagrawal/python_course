# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:35:07 2019

@author: Education
"""
import os
from PIL import Image
'''img = Image.open("20170211_220907.jpg")
img.save("img.png")                           #to change the format of a image
img.show()'''


fileList = os.listdir("D:/forsk")

for image in fileList:
    if (image.endswith(".png")):
            with open(image) as img:
             img.thumbnail(list(map(int,input(">height,width ").split(","))))       
             img.show()
       
         