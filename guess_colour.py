#!/usr/bin/python3

"""
    Program: guess_colour.py
    Purpose: Evaluate matching colours
    Date and version: Sept 16, 2025 - version 1
    Author: Joey Mainwaring
"""

# Prompt user for input
colour = input("Guess the colour of Alongquin College (Enter q to quit): ").lower()

# Loop until colour guessed
while colour != "q" and colour != "green":
    colour = (input("That it not correct, please guess again: ")).lower()

#Exit statement
print("You guessed correct! Algonquin College team spirit is Green!")
