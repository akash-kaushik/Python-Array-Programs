# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:37:59 2020

@author: Akash Kaushik
"""


def user_input():
    
    number = "wrong"
    
    while number.isdigit() == False:
        number = input()
        
    return int(number)

print("Enter the length of an Array:")
l = user_input()

my_array = []

def array_input(l,my_array):
    
    for i in range(0,l):
        print("Enter the", (i+1), "value of an array:")
        my_array.append(user_input())
        
    return my_array

new_array = []
new_array = array_input(l, my_array)

rotated_array = []

def rotation_of_array(new_array):
    
    rotated_array = new_array[::-1]
    
    return rotated_array

print("Rotated Array:", rotation_of_array(new_array))