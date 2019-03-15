# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:45:44 2019

@author: Education
"""
#thanksgiving analysis

import pandas as pd      #import pandas
import numpy as np 

df = pd.read_csv("thanksgiving.csv",encoding = "Windows 1252")

#df.columns = ["RespondID","CelebrationRespond","DishType","DishCokked","Stuffing","CranebarrySauce","Gravy","SideDish","SideDishServedCarrot","SideDishServed","SideDishServedCorn","SideDishServedCornBread","SideDishServedFruitSalad","GreanBeans","Macroni","MashedPotatos","Rolls/Biscuits","VegeTableSalad","Yams/SweetPotato","Vinagratee","Apple","ButterMilk","Cherry","Chocolate","Peach","Pecan","Pumpkin","SweetPotatos","Other","Fruits","Blondies","Brownies","CarrotCake","ChesseCake","Cookies","Fudge","IceCream","Cobbler","JellyRole","Option","TravelDistance","KidsCutOff","MeetUp","BlackFriday","RetailWork","EmployeerWorkBF","Region","Age","Sex","Income","State" ]


df.columns = [i for i in range(0,65)] #conversion of column name into a single name

df_ref = dict(zip([i for i in range(0,65)],df.columns))   #reference of labeling

df_pattern = df.groupby([60,63])[2]  #eating pattern

df_income_hom = df[63][df[8] =="Homemade"].value_counts()   #comparison of income

df_income_hom_new = df[63][df[8] =="Canned"].value_counts()   #comparison of income

df_avg = df[8].value_counts().mean()   #Each type of source

#df_comp = df[60][(df[2]=="Turkey") & (df[60] == "Suburban")].count() #eating SuburBan area

#df_comp_new = df[60][(df[2]=="Turkey") & (df[60] == "Rural")].count() #eating Rural area

df_count = df[60][df[2]=="Turkey"].value_counts()   #counting those which nelomgs to different arae and eat turkey
                      
Black_Friday = df[57].value_counts()   #Black friday

df_grpw = df.groupby([63])[df[8]=="Homemade"].count()  #Homemade  income

df_pattern_veri = df[63][(df[2]=="Turducken") & (df[8]=="Homemade")].value_counts()  #income who eat turuducken and homemade sauce

df_carn = df[63][(df[8] == "Canned")].value_counts() #income who eat Canned

df_roast = df[63][(df[4] == "Roasted")].value_counts()  #income who eat roasted

df_count = df.groupby([60]).count()    #number of people eat different kind of dishes

df[63].dtypes
def gender_filter(value):
    if value =="Female":
        return "Male"
    elif value == "Male":
        return "Female"
    else:
        pass
    
df[62] = df[62].apply(gender_filter)

df[63] = df[63].replace(np.nan,"Missing")    #replace missing value by Missing
def income_filter(income):  
  income = income.replace(",","").replace("$","")  
  if income == "Missing" or income =="Prefer not to answer":
      return income
  elif income == "200000 and up":
      income = income.split()
      for i in income:
       if i.isdigit():
        income = int(income[0])
        return income
  else:
      income = income.replace("to",",").split(",")
      #income = income.split(",")
      income[0] = int(income[0])
      income[-1] = int(income[-1])
      income = (income[0]+income[-1])/2
      return income  

df[63] = df[63].apply(income_filter)    # .apply methiod on 63 column


np.lstsq()

