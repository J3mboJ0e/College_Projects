#!/usr/bin/python3

"""
    Program: exponentiate.py
    Purpose: To square and cube an interger
    Date and Version: Oct 3 2025 - version 1
    Author: Joey Mainwaring
"""

# Function to prompt user for a number
def get_integer(user_prompt="Please enter a whole number: "):
    return int(input(user_prompt))

# Function to square a number
def square(number):
    return number * number

# Function to cube a number
def cube(number):
    return number ** 3

# Display Message
print("This program squares and cubes an whole number for you")

# Ask user to proceed or quit
response = input("would you like to proceed using the program?, press y for yes and n for no: ")

# Loop through the main function
while response == "y":
    number = get_integer()
    if number == 0:
        print("0")
    elif number == 1:
        print("1")
    else: 
        print(f"the square of the {number} is {square(number)} and the cube of the {number} is {cube(number)}")   
   
    # Re-ask user to proceed or quit
    response = input("would you like to proceed using the program?, press y for yes and n for no: ")

# Closing Statement
print("Thanks for using the exponentiate program")
