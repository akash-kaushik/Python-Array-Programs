# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:48:11 2020

@author: Akash Kaushik
"""

def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
    return int(number)


print("Enter the length of an Array:")
l = user_input()

def array_input(l):
    
    my_array = []
    
    for i in range(0,l):
        print("Enter the", (i+1), "value of an Array:")
        my_array.append(user_input())
        
    return my_array

new_array = []
new_array = array_input(l)

print("Enter the value of Array Rotation:")
n = user_input()

def array_rotation(new_array,n):
    
    rotation_part = new_array[:n]
    sec_rotation_part = new_array[n:]
    rotated_array = sec_rotation_part + rotation_part
    
    return rotated_array

print("Array =", new_array)
print("Reversal Array =", array_rotation(new_array,n))
        