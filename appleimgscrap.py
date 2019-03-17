# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:02:15 2019

@author: Education
"""

#image scarraping

# scrap the apple image
from selenium import webdriver     #import selenium

import urllib
  
wiki = "https://www.istockphoto.com/my/photos/apple?sort=mostpopular&mediatype=photography&phrase=apple"

driver = webdriver.Chrome("C:/Users/Education/Documents/Downloads/chromedriver")     #set the path of chrome Driver

driver.get(wiki)     #get the data from the url

image = driver.find_element_by_class_name("unzoomed")

img = image.find_element_by_tag_name("img")

im = img.get_attribute('src')

urllib.request.urlretrieve(im,"appleimage.png")    #scrapping of a image through a link