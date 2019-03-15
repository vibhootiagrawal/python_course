# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:30:38 2019

@author: Education
"""
#creation of random array of 40 integers between 5-15 udsing numby and count the frequency of numbers

import numpy as np    #import  numpy

from collections import Counter   #import Counter class ffrom collectons module

array = np.array(np.random.randint(5,15,40))   #random array generation  

count = Counter(array)  #count the frequency of each number without using numpy


#count the frequency of an element using numpy
unique_elements, counts_elements = np.unique(array,return_counts=True)

count_value = np.asarray([unique_elements,counts_elements])
