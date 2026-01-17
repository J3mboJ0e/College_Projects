#!/usr/bin/python3

"""
    Program: parity_ctr.py
    Purpose: To count even and odd numbers
    Date and version: Sept 23 2025 - version 1
    Author: Joey Mainwaring
"""

# Initilize the counters
counter_odd = 0
counter_even = 0

# Prompt user for number
number = int(input("Enter a number or press 0 to quit: "))

# Initialize while loop
while number != 0: 
    if number % 2 == 1:
        counter_odd += 1
    else:
        counter_even += 1
    number = int(input("Enter a number or press 0 to quit: "))

# Display count
print("odd:", counter_odd, "even:", counter_even)

# Closing statement
print("Cheers mate")
