# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:24:20 2019

@author: Education
"""

#convert jsondata into our python program
import json

jsonData = """[{
	"faculty": [{
			"f-name": "Anuja",
			"l-name": "Daas",
			"Contact": [{"mob1": 907446883}, {"mob2": 6347375231,"basic": 654684}],
			"E-mail": [{"Clg": "anuja@jecrcu.edu.in"}, {"personal": "anuja1@gmail.com"}]
		},
		{
			"f-name": "Meghna",
			"l-name": "Jain",
			"Contact": {"mob1": 907445683,"mob2": 6347375231,"basic": 654684},
			"E-mail": [{"Clg": "anuja@jecrcu.edu.in"}, {"personal": "anuja1@gmail.com"}]
		}
	]},
	{"student": [{
			"f-name": "Vibhooti",
			"l-name": "agrawal",
			"contact": {"m1": [{"m2": 7547459958,"Basic": 47856}]}
		},
		{
			"f-name": "Meenal",
			"l-name": "Goyal",
			"contact": {"m1": [{"m2": 7547459958,"Basic": 47856479}]}
		}
	]
}
]
"""
print(type(jsonData))

myJson = json.loads(jsonData)

print(type(myJson))

print(myJson[0]["faculty"][0]["f-name"])

jsonNew = json.dumps(myJson)

print(type(jsonNew))