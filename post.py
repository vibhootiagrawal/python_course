# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:01:17 2019

@author: Education
"""
"""post method basically used to post means send the
 data to a perticular server or store it in a
 database ,post method also used to reterive the data 
 for this we do "/post" within our url by default server send the data by get method
 while get method to reterive the data from 
 the database and with the get method we can also send 
 the information in the querry form syntax like that:
 key = value,key define what would be the header 
 and value define what would be the value of that key"""
 
 
 
""""header : basically a informative part which inform about where data will be store time like that
    payload : it is the body part which will be send 
    host:it is the main url"""
 


import requests,json

payLoad = {"firstName":['vibhooti','yash','deepak'],"Language":["English","Spanish","chienese"]}

#payLoad = json.dumps(payLoad)

Header = {'Content-Type':'application/json','port':80,'Protocoal':"HTTP","content_length":len(payLoad)}


def post():
    Host = "http://httpbin.org/post"
    postMy = requests.post(Host,payLoad,Header)
    return postMy

resp = post()
print(resp.text)
print(resp.headers)

def get():
    url = "http://httpbin.org/get?firstName=Vibhooti&MEENAL&language=hindi"   
    
    params = {'firstName':"Piyush",'language':'german'}                     #by this we can receive and send data in this
                                                                            #we can send it either passing in url or by passing
                                                                            #as a parameter with url if we pass it in both it return both
                                                                            #what work get and post perform it depend upon API that what action API perform display,read or any other supported functionality    
    response = requests.get(url,params)
    
    
    jsonData = response.json()
    
    return jsonData
    
    response.close
    print("Headers:" ,response.headers)
   

     
print(get())