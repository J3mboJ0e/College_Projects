#!/usr/bin/python3

"""
    Program: guess_course.py
    Purpose: To evaluate user input repeatedly
    Date and version: Sept 16, 2025 - version 2
    Author: Joey Mainwaring
"""

COURSE_CODE = "CST8245"

# User prompt for input
course = input("Please enter the course code (or press q to quit): ")

# Loop until course code guessed
while course != "q" and course != COURSE_CODE:
    course = input("That is not correct, please guess again (or press q to quit): ")

# Closing statement
print("Thank you for guessing the course!")
