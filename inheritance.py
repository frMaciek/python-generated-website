# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 04:43:29 2018

@author: maciej
"""

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")        
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        
class Child(Parent):
    print("Child Constructor Called")   
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))
        
billy_cyrus = Parent("Cyrus", "green")
billy_cyrus.show_info()
#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()