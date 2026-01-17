#!/usr/bin/python3

"""
    Program: guess_number.py
    Purpose: guess the same number multiple times until correct or quit
    Date and version: September 27, 2025 - version 1
    Author: Joey Mainwaring
"""

# Generate a secret number
import random
secret = random.randint(1,9)

# Prompt user for guess
guess = int(input("Enter a number between 1 and 9, or press 0 to quit: "))

# Loop while user attempts to guess secret number
while guess != secret and guess != 0:
    if guess < secret:
        print("The secret number is higher")
    elif guess > secret:
        print("The secret number is lower")
    guess = int(input("Please guess again: "))
    
# User guesses correctly    
if guess == secret:
    print("Congratulations on guessing the correct number!")
elif guess == 0:
    print("I am sad to see you go")
       
# Closing Statement
print("Have a great day")
