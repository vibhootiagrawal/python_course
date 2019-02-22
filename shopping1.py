# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:36:18 2019

@author: Education
"""

item_list = []
item1 = "NULL" 

def enter():
 while True:    
     item = input(">  ")
     if (item.upper()=="DONE"):
         break
     item_list.append(item)
     
 choice=input("r u want to perform more action: ")       #enter choice
 
 if(choice.upper()=="YES"):
    func()
 else:
     print("Done")
        
     
def show():
    for i in item_list:
        print(i)
    choice = input("r u want to do something: ")       #enter choice
    
    if(choice.upper()=="YES"):
         func()
    else:
        print("Done")    
        
        
        
def Help():
      print("show:it is used to show the item in item_list")
      print("DONE:to quit from the loop")
      print("iNDEX: insert item at a perticular index")
      print("rEMOVE:remove the item ")
      print("file:read all the data in file")
      
      choice = input("r u want to do something: ")       #enter choice
      
      if(choice.upper()=="YES"):
         func()
      else:
          print("Done") 
      
      
def index():
 x = int(input("enter index"))
 for i in item1:
    if i not in item_list:
        item_list.insert(x,i)
    else:
        pass  
 print(item_list)
 
 choice = input("r u want to do something: ")       #enter choice
 
 if(choice.upper()=="YES"):
         func()
 else:
        print("Done") 

 
def remove(): 
    for i in item1:
     if i in item_list:
       item_list.remove(i)
     else:
         pass
    print(item_list) 
    
    choice = input("r u want to do something: ")       #enter choice
    if(choice.upper()=="YES"):
         func()
    else:
        print("Done") 
    
def file():   
 try:
    f = open("progrm.txt","w")
    for i in item_list:
      f.write(i)  
    f.close()
    f = open("progrm.txt","w")
    f.read()
 except:
    pass 
 choice=input("r u want to do something: ")       #enter choice
 
 if(choice.upper()=="YES"):
         func()
 else:
        print("Done") 
        
 def func():
  choice = input('''Show is used to show the items,
                    press help for more info,
                    index for adding new iteam at specific index,
                    remove to remove a item, 
                    file is used to read all items: ''')
  try:
      
     if(choice.upper()=="SHOW"):
       show()
       
     elif (choice.upper()=="ENTER"):
        enter()
        
     elif(choice.upper()=="HELP"):
       Help() 
       
       
     elif(choice.upper()=="INDEX"):
        item1 = input("> ").split(",")
        index()
        
        
     elif(choice.upper() =="REMOVE"):
        remove()
        
        
     elif(choice.upper()=="FILE"): 
        file()
        
     else:
        pass
    
  except Exception as e:
    print(e)
    
  finally:
    print("your program will end")    
    
print('''welcome to my app
         Help -> Help
         Enter-> Enter
         Other-> Other''')    

choice=input("> ")       #enter choice

if(choice.upper()=="HELP"):
    Help()
    
else:
    my = input("to perform more functionality yes otherwise press Done:")  
    
    if(my.upper()=="YES"):
      func() 
        
    elif(choice.upper()=="ENTER"):
     enter() 
    
    elif(choice.upper()=="OTHER"):
      func()
       
    else:
     print("quit")  
    
    

