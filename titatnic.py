# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:44:27 2019

@author: Education
"""
#Automobile Analysis
import pandas as pd   #import pandas

#value_counts() work on a series not a dataframe while groupby work on a datframe

df = pd.read_csv("training_titanic.csv")   #read the csv file we can read any url or text or any other extension file using this method

#df['Survived'].count()      #count all values


#df.groupby(['Survived']).groups  #group according the specific condition

#df_count = df['Survived'][df['Survived']==0].value_counts()    #cont values        #0 - means no.if died people
                                                                # 1 - means no.of pople survived

#df_count = df[['Survived','Sex']].value_counts()

#df_per = df["Survived"][(df["Sex"] == "female") & (df["Survived"] == 0)].value_counts()


#Number of people whomis died and live
df_count = df["Survived"].value_counts()    #count number of people died and survived                                                            

df_alive = df["Survived"][df["Survived"] == 1].value_counts()  #number of people who is survive

df_died = df["Survived"][df["Survived"] == 1].value_counts()   #number of people who is died

df_alive_female = df["Survived"][(df["Survived"] == 1) & (df["Sex"] == "female")].value_counts().describe()     #percent of female who is alive 
 
df_died_female = df["Survived"][(df["Survived"] == 0) & (df["Sex"] == "female")].value_counts().describe()      #percent of female who is died 

df_alive_male = df["Survived"][(df["Survived"] == 1) & (df["Sex"] == "male")].value_counts().describe()     #percent of male who is alive 

df_died_male = df["Survived"][(df["Survived"] == 0) & (df["Sex"] == "male")].value_counts().describe()     #percent of male who is died
 