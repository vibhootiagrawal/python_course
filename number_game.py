# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:42:45 2019

@author: Education
"""

import random
secret_number=random.randint(1,10)
chance=0
def chancer(): 
  n=6
  if(n>0):  
    chance=n-1
    n=n-1
    return chance

def gamer(): 
  guess_number=int(input("enter number"))  
  if(guess_number>0):
    if(secret_number==guess_number):
      print("player wins and computer loss")
    else:  
      print("player loss and computer wins")    
      print("secret_number{},guess_number{}".format(secret_number,guess_number))
      if(guess_number>secret_number):
        print("too High")
      elif(guess_number<secret_number):
       print("too LOW")
      #else:
        #pass
      a=chancer()
      print("number of try left",a)
      for i in range(1,6):
         option=input("do u want to play again:")
         if(option=="play again"):
           gamer()
         else:
            break
        
  else:
    print("number is not integer")

gamer()
if(secret_number!=guess_number):
  for i in range(1,6):
         option=input("do u want to play again:")
         if(option=="play again"):
           gamer()
         else:
            break
else:
         option=input("do u want to play again:")
         if(option=="play again"):
           gamer()
         else:
            print("quit")
