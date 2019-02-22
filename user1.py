# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:33:12 2019

@author: Education
"""

#gravity_cal problem
 #gravity_cal problem
Acceleration=int(input("enter acceleration"))
Time_sec=int(input("time"))
Object_position=int((Acceleration*Time_sec*Time_sec)/2)
print(Object_position)

#mileage
Travel_km=int(input("Kilometer"))
cost_per_litre=int(input("liter"))
average_rate=int(input("average_rate"))
Driving_cost=((Travel_km/average_rate)*cost_per_litre)
print(Driving_cost)


 #temprature problem
Temprature_centigrade=int(input("enter centigrade Temp.")) #jaipur temprature
Temprature_farenheight=(29*(9/5)+32)
print(Temprature_farenheight)
Temprature_kelvin=29+273
print(Temprature_kelvin)


#score problem
A1=int(input("marks ass."))
A2=int(input("marks ass."))
A3=int(input("marks ass."))
E1=int(input("marks Exam"))
E2=int(input("marks Exam"))
Weighted_score=(A1+A2+A3)*(10/100)+(E1+E2)*(35/100)   #if respective Weight of each assignment is 10% and each eaxm is 35 %
print(Weighted_score)

#read_cost
Travel_km=int(input("enter km."))
cost_per_litre=int(input("cost per liter"))
average_rate=int(input("enter rate"))
Driving_cost=(80/18)*80
print(Driving_cost)


#heart beat problem
age=int(input("enter age"))
maximum_heart_rate=220-21
lower_end_heart_rate=maximum_heart_rate*0.7
Higher_end_heart_rate=maximum_heart_rate*0.85
print(maximum_heart_rate)
target_heart_rate_range=str(lower_end_heart_rate)+"_"+str(Higher_end_heart_rate)
print(target_heart_rate_range)



#height
Height_foot=int(input("enter height in foot"))
Height_inch=int(input("enter height in inch"))
height_calculator=(5*0.3048+11*0.0254)
print(height_calculator)
height_calculator=(height_calculator)*100
print(height_calculator)



#bmi 
weight=int(input("enter weight in kg"))#in kg
height=int(input("enter height"))
bmi_cal=weight/(height*height)
print(bmi_cal)


#height
height_foot=int(input("enter height in foot"))
height_inch=int(input("enter height in inch"))
height_calculator=(height_foot*0.3048+height_inch*0.0254)
print(height_calculator)
height_calculator=(height_calculator)*100
print(height_calculator)