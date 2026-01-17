#!/usr/bin/python3

"""
    Program: adder.py
    Purpose: Create and call a function: two arguments and a return value
    Date and version: Oct 3 2025 - version 1
    Author: Joey Mainwaring
"""

# Define function
def add(number_1, number_2):
    sum = number_1 + number_2
    return sum

# User prompt
number_1 = float(input("Please enter a number: "))
number_2 = float(input("Please enter another number: "))

# Function call
result = add(number_1, number_2)

# Result
print(result)
