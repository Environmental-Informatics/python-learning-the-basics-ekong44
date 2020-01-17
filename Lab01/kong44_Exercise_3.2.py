"""
Eric Kong
ABE 651
1/15/20
Think Python Exercise 3.2

Personal reference for a good site that describes the idea of function and objects: 
https://www.i-programmer.info/programming/python/12437-programmers-python-function-objects.html
"""

# this function accepts 2 arguments
def do_twice(arg1,val1):
    arg1(val1)
    arg1(val1)

# #this function accepts a string and prints it twice
def print_twice(string):
	print(string)
	print(string)

# combines the earlier functions 
# two times two is equal to four
do_twice(print_twice,"spam") # a function within another function (function object)