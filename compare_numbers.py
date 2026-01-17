#!/usr/bin/python3

"""
    Program: compare_numbers.py
    Purpose: Evaluate the higher of two numbers
    Date and version: Sept 15, 2025 - version 1
    Author: Joey Mainwaring
"""

# Prompt user for numbers
num_1 = int(input("Please input a number: "))
num_2 = int(input("Please input a second number: "))

# Compare the two numbers
if num_1 > num_2:
    print("The higher number is:", num_1 )
elif num_1 < num_2:
    print("The higher number is:", num_2)
else:
    print("The numbers are equal")

#Closing statement
print("Good-bye Friend")
