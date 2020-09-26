# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:54:27 2020

@author: Akash Kaushik
"""


def user_input():
    number = "wrong"
    
    while number.isdigit() == False:
        number = input()
        
    return int(number)



print("Enter the length of the array:")
l = user_input()

my_array = []

sum1 = 0 

def array_input(l,my_array):
    
    
    for i in range(0,l):
        print("Enter ", (i+1), "value of array:")
        my_array.append(user_input())
        
    return my_array

new_array = []
new_array = array_input(l,my_array)

for i in range(0,l):
    sum1 = sum1 + new_array[i]



print("Array = ", new_array, "\nSum =", sum1)