# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:47:09 2019

@author: Education
"""

#scrap the image
from selenium import webdriver

import urllib

wiki = "https://media.istockphoto.com/photos/red-apple-with-leaf-picture-id683494078"

driver = webdriver.Chrome("C:/Users/Education/Documents/Downloads/chromedriver")

driver.get(wiki)

image = driver.find_element_by_tag_name("img")

img = image.get_attribute('src')

urllib.request.urlretrieve(img, "filename.jpg")