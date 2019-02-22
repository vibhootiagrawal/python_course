# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:28:46 2019

@author: Education
"""

with open("progrm.txt","rt") as file:
    with open("Copy.txt","wt") as new_file:
        for line in file:
            new_file.write(line)
            