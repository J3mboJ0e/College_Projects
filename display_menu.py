#!/usr/bin/python3

"""
    Program: display_menu.py
    Purpose: to create and call a function: one argument and a return value
    Date and version: Oct 3 2025, version - 1
    Author: Joey Mainwaring
"""

# Funtion Definition
def show_menu():
    print("Drinks")
    print("Appetizers")
    print("Soups and Salads")
    print("Mains")
    return

def get_menu_choice(menu_selection):
    user_choice = input(menu_selection)
    return user_choice

# Call Functions
show_menu()
user_choice = get_menu_choice("Please select a menu option: ")
