#!/usr/bin/python3

"""
    Program: simple_calculator.py
    Purpose: to calculate simple mathematical problems
    Date and version: September 27, 2025 - version 1
    Author: Joey Mainwaring
"""

# Prompt user for operator
operator = input("Enter operator [+, -, *, /] (q to quit): ")

# Start of loop
while operator.upper() != "Q":

# Prompt for operands.
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))

# Calculate numbers based on operator selection.
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        while number_2 == 0:
            number_2 = float(input("Please enter a number greater than 0: "))
        result = number_1 / number_2

# Display result of calculation.
    print( "-> Result of:", number_1, operator, number_2, "=", result)

# Reprompt for operator.
    operator = input("Enter operator [+, -, *, /] (q to quit): ")

#Closing Statement
print("Closing calculator")
