# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:34:21 2019

@author: Education
"""
#access the result of kerla board result

from selenium import webdriver     #import webdriver from selenium 

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

driver = webdriver.Chrome("C:/Users/Education/Documents/Downloads/chromedriver")

driver.get(wiki)    # Opening the submission url

Head = driver.find_element_by_class_name("firstHeading")     #access the Head usig selenium
print(Head.text)

para = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')    #access the para using paragraph

print(para)

required_list = driver.find_element_by_class_name("toc")

required_ul = required_list.find_element_by_tag_name("ul")   #access the table using selenium

print(required_ul.text)

required_data = driver.find_element_by_class_name("hlist")

required_ul_my = required_data.find_element_by_tag_name("ul")

print(required_ul_my.text)

