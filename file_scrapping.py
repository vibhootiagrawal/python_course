# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:04:30 2019

@author: Education
"""

from selenium import webdriver

url = "https://community.periscopedata.com/t/18bzry/test-for-normal-distribution-of-data-with-python"

driver = webdriver.Chrome("C:/Users/Education/Documents/Downloads/chromedriver")

driver.get(url)

file_data = driver.find_element_by_xpath('//*[@id="18bzry"]/div/div[2]/span[1]/a')  
   
file_data.click() 
