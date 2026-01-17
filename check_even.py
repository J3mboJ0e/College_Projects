#!/usr/bin/python3

"""
    Program: check_even.py
    Purpose: Create and call a function: one argument and a return value of True/False
    Date and version: Oct 3 2025 - version 1
    Author: Joey Mainwaring
"""

# Function Definitions
def iseven(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Prompt for an interger
number = int(input("Please input a number: "))

# Function call
if iseven(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
