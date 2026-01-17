#!/usr/bin/python3

"""
    Program: select_operatorpy
    Purpose: Execute an operation based on user selection
    Date and version: Sept 16, 2025 - version 1
    Author: Joey Mainwaring
"""

# Prompt user for input
operator = input("Please select one of the following arithmetic operators [+, -, *, /]: ")

# For addition
if operator == "+":
    print("Addition")

# For subtraction
elif operator == "-":
    print("Subtraction")

# For Multuiplication
elif operator == "*":
    print("Multiplication")

# For division
elif operator == "/":
    print("Division")

# For no operator input
else:
    print("Invalid selection")

# Closing statment
print("Thank you")
