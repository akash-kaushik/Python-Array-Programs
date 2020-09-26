# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:38:15 2020

@author: Akash Kaushik
"""


def user_input():
    
    number = "wrong"
    
    while number.isdigit() == False:
        number = input()
        
        
    return int(number)

print("Enter the length of an ARRAY:")
l = user_input()

def array_input(l):
    my_array = []
    
    for i in range(0,l):
        print("Enter the", (i+1), "value of an array:")
        my_array.append(user_input())
        
    
    return my_array

new_array = []
new_array = array_input(l)

def array_mlt(new_array,l):
    
    mult = 1
    
    for i in range(0,l):
        mult = mult * new_array[i]
        
    return mult

mulltip = array_mlt(new_array,l)

print("Enter the value of Divider:")
div = user_input()


rem = mulltip % div

print("Multiplication =", mulltip, "\nReminder =", rem)


        