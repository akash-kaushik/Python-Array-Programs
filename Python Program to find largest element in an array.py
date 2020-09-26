# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:26:39 2020

@author: Akash Kaushik
"""


def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
    return int(number)

print("Enter the length of an Array:")
l = user_input()

my_array = []

def array_input(l,my_array):
    
    for i in range(0,l):
        print("Enter the", (i+1), "value of array:")
        my_array.append(user_input())
        
    return my_array

new_array = []
new_array = array_input(l, my_array)

def find_largest_number(new_array):
    
    n = 0
    for i in range(0, l):
        
        if new_array[i] > n:
            n = new_array[i]
            
        else:
            n = n
    
    return n

lar_num = find_largest_number(new_array)

print("Array =", new_array, "\nLargest number:", lar_num)