#!/usr/bin/python3

"""
   Program: summate_numbers.py
   Purpose: addition of numbers
   Date and version: Sept 16, 2025 - version 1
   Author: Joey Mainwaring
"""

# Variables
sum = 0

# Prompt user for a number
addend = int(input("Enter an interger (0 to quit): "))

# Loop to continously add numbers
while addend != 0:
   sum += addend
   addend = int(input("Enter an interger (0 to quit): "))

# Display sum
print("The total is:", sum)
