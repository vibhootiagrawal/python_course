# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:56:31 2019

@author: Education
"""


import pandas as pd      #import pandas

my_list = [[23,34],[67,89]]

df_pra = pd.DataFrame(my_list,columns=["A","B"],index = [1,2])

#it insert new column in the dataframe
df_pra["Add"] = 1

df_pra["Column"] = [3,4]

#drop a column from the dataframe
df_pra = df_pra.drop("Add",axis = 1)

#insert a new column at perticular index
df_pra.insert(loc=1,column = 'new',value=[10,20])

unique = pd.unique(df_pra["A"])    #to get unique value in dataframe it preserved the order 
