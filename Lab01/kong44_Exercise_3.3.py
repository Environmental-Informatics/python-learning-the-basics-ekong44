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
do_once(print_once,"+ - - - - + - - - - +")
do_twice(print_twice,"|         |         |") 
do_once(print_once,"+ - - - - + - - - - +")
do_twice(print_twice,"|         |         |") 
do_once(print_once,"+ - - - - + - - - - +")

##################################################################
print("--------------------Dividing Line--------------")
