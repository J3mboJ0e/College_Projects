#!/usr/bin/python3

"""
    Program name: calc_sequential.py
    Program purpose: perform arithmetic operations
    Author: Joey Mainwaring
    Date & version: September 09 2025, version: 3.0
"""

# Greet user.
name = input("Enter your name: ")
print("Hello", name)

# Request user operands.
operand_1 = float(input("Enter a number: "))
operand_2 = float(input("Enter a second number: "))

# Arithmetic calculations
sum = operand_1 + operand_2
print("Result of additions as float:", float(sum), ", as int: ", int(sum))
difference = operand_1 - operand_2
print("Result of subtraction as float:", float(difference), ", as int: ", int(difference))

# Closing statement
print("Thank you", name, "for playing")
