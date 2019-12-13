# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 04:00:16 2019

@author: HP
"""

#x=1  #int
#
#y=2.5 #float
#
#name='Hemant' #str
#
#is_cool=True #bool
#
#Multiple Assignment
#
#x,y,name,is_cool=(1,2.5,'Hemant',True)
#
#print('Hello')
#
#x=6
#y=20
#
#numbers=[1,2,3,4,5]
#
#if x not in numbers:
#    print(x not in numbers)
#
#
#people=['John','Paul','Sara','Susan']
#
#for person in people:
#    print(f'Current person: {person}')
#    

#
#people=['John','Paul','Sara','Susan']
#
#for person in people:
#    if person=='Sara':
#        break
#    print(f'Current person: {person}')
#    

#
#for i in range(len(people)):
#    print(people[i])
#
#for i in range(0,11):
#    print(f'Number:{i}')
#    



#today=datetime.date.today()
#print(today)
#
#from datetime import date
#from time import time
#
#today=date.today()
#timestamp=time()
#
#print(timestamp)
##
#from validator import validate_email
#
#email='test@test.com'
#if validate_email(email):
#    print('Email is valid')
#else:
#    print('Email is bad')


#class User:
#    def __init__(self,name,email,age):
#        self.name=name
#        self.email=email
#        self.age=age
#    
#    def greeting(self):
#        return f'My name is {self.name} and I am {self.age}'
#
#    def has_birthday(self):
#        self.age+=1
#
#class Customer(User):
#    def __init__(self,name,email,age):
#        self.name=name
#        self.email=email
#        self.age=age
#        self.balance=0
#    def set_balance(self, balance):
#        self.balance=balance
#    
#
#
#hemant=User('Hemant Bhadoria', 'hemant@gmail.com',38)
#
#rohan=Customer('Rohan Shanbhaag', 'rohan@gmail.com',32)
#rohan.set_balance(500)
#print(rohan.greeting())
#
#hemant.has_birthday()
##print(hemant.greeting())
##
#
#myFile=open('myfile.txt', 'w')
#print('Name:', myFile.name)
#print('Is closed: ',myFile.closed)
#print('Opening Mode:', myFile.mode)
#
#myFile.write('I love Python')
#myFile.write('and JavaScript')
#myFile.close()
#
#myFile=open('myfile.txt', 'a')
#myFile.write('I also like PHP')
#myFile.close()
#
#myFile=open('myfile.txt','r+')
#text=myFile.read(100)
#print(text)


import json

userJSON='{"first_name":"John","last_name":"Doe","age":30}'

user=json.loads(userJSON)

print(user)
print(user['first_name'])

car={"make":'Ford', 'mode':'Mustang', 'year':1970}

carJSON=json.dumps(car)
print(carJSON)












