# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:30:48 2019

@author: Education
"""

f=open("progrm.txt","rb")
f.seek(-3,2)      #to work with 1,2 seek value either we open the file in binary format or put the first argument means from where we start reading always 0 
f.read()


import zlib    #we have to convert a string in byte format first for this we have to write for type conversion

s = b"Python is used extensively in industry. BSDU is currently running an an industry oriented in Python in colloboration with Forsk Technologies"

len(s)

t = zlib.compress(s)
len(t)

s1 = zlib.decompress(t)


import urllib2

f = urllib2.urlopen("http://www.google.com/")

f.read(1000)

from PIL import Image

# Saving the file in different format
img_filename = Image.open ("sample1.jpg")
img_filename.show ()

