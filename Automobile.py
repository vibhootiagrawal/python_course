# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:56:15 2019

@author: Education
"""

import pandas as pd
 
df = pd.read_csv("Automobile.csv")

df["price"].values       #get the value from price column into numpy.ndarray

df["price"].describe()    #max,min,avg,standrad daviation 