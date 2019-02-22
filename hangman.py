# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:28:12 2019

@author: Education
"""

import random

list1 = ['grapes', 'orange', 'apple', 'papaya', 'tomato', 'Branjil', 
       'anjeer', 'banana', 'tomato', 'cabagge', 'penuts']

Name = random.choice(list1)
y=list(" "*len(Name))

try:
 def Hangman():
  for i in range(6,-1,-1):
    playerguess=input("enter guess: ")
    if playerguess in Name:
        print("player wins")
        x=Name.index(playerguess)
        y.insert(x,playerguess)
    else:
        print("player loss") 
    print("number of chances left:",i )
    
 Hangman()  
 choice=input("do u want play again yes or no: ")
 if(choice.upper()=="YES"):
     Hangman()
 else:
     print("Quit the Hangman")
except Exception as e:
    print("Exception:",e)
    
else:       
 for i in y:
   print(i,end=" ")     

finally:
  print("\n Hangman Game")      