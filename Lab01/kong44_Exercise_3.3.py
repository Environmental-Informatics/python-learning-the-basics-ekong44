#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 23:21:28 2020
@author: kong44

ABE651
Think Python Exercise 3.3

Building on Exercise 3.2
Using function and strings to print the object below:
    
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

"""
plus_line = "+ - - - - + - - - - +"
pipe_line = "|         |         |"
plus_line2 = plus_line*2
pipe_line2 = pipe_line*2

# this function accepts 2 arguments
def do_once(arg0,val0):
    arg0(val0)

# this function accepts 2 arguments
def do_twice(arg1,val1):
    arg1(val1)
    arg1(val1)

# this function accepts a string and prints it twice
def print_twice(string):
	print(string)
	print(string)

# prints a string once
def print_once(string2):
    print(string2)

# printing the shape
# combines the earlier functions 
def single_shape(do_once,do_twice):
    do_once(print_once, plus_line)
    do_twice(print_twice,pipe_line) 
    do_once(print_once,plus_line)
    do_twice(print_twice,pipe_line) 
    do_once(print_once,plus_line)
    
def grid_shape(do_once,do_twice):
    do_once(print_once, plus_line2)
    do_twice(print_twice,pipe_line2) 
    do_once(print_once,plus_line2)
    do_twice(print_twice,pipe_line2) 
    do_once(print_once,plus_line2)

single_shape(do_once,do_twice) #runs the single shape function 

##################################################################
print("\n\n--------------------Dividing Line--------------")
print("---------------------Part 2 Below------------------\n")

grid_shape(do_once,do_twice)
grid_shape(do_once,do_twice)

##################################################################
print("\n\n--------------------Dividing Line--------------")
print("-----------Personal Practice Below, uncomment to see--------\n")

# playing around 
# using what I learned from Learn Python The Hard Way to prompt the user
# =============================================================================
# grid_question = input("Do you want to print a larger grid (Y or N?)\n")
# 
# if grid_question == "Y":
#     grid_shape(do_once,do_twice)
#     grid_shape(do_once,do_twice)
#     
# else: 
#     quit()
# =============================================================================
    
