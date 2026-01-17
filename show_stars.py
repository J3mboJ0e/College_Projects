#!/usr/bin/python3

"""
    Program: show_stars.py
    Purpose: To display an X nubmer of stars
    Date and version: Sept 16, 2025 - version 1
    Author: Joey Mainwaring
"""

# For loop code
num_stars = int(input("Enter number of stars: "))
for i in range(0, num_stars):
    print("*", end="")
print()
