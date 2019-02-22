# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:23:50 2019

@author: Education
"""

import random
secret_number=random.randint(1,10)
def gamer():
     guess_number=int(input("enter number"))
     if(secret_number==guess_number):
         print("player wins computer loss")
     else:   
         print("player loss computer wins")
         print("secret_number{},guess_number{}".format(secret_number,guess_number))
         if(secret_number>guess_number):
             print("too HIGH")
         else:
            print("too LOW")
        
gamer() 
for i in range(6,0,-1): 
   print("number of chance left",i)       
   choice=input("do u want to play again")
   if(choice=="yes"):
       gamer()
   else:
      break    
         
         