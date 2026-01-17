#!/usr/bin/python3

"""
    Program: sql_query.py
    Purpose: Query a Library Database
    Date and version: Nov 22 2025 - version 1
    Author: Joey Mainwaring
"""

# Imports
import sys
import psycopg2

# Constants
NAME = "lib_main0144"
ROLE = "dbadmin"

# Function Definitions
def show_menu():
    print("Library Database")
    print("1. Display all books")
    print("2. Display a member")
    print("Q. Quit")

def get_menu_option(prompt):
    return input(prompt)

def display_query():
    """Fetch and display query results."""
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")

def query_lastname(last_name):
    """Display member info for a given last name."""
    sql = """
    SELECT member_id, last_name, first_name, phone
    FROM member
    WHERE last_name = %s;
    """
    cursor.execute(sql, (last_name,))
    display_query()

def get_lastname():
    return input("Enter member last name: ").strip()

def query_books():
    """Display all books sorted by title."""
    sql = """
    SELECT title, isbn, rental_days
    FROM book
    ORDER BY title ASC;
    """
    cursor.execute(sql)
    display_query()

# Establish database connection
try:
    connection = psycopg2.connect(database=NAME, user=ROLE)
except psycopg2.DatabaseError:
    print("Error: Connection to database not established.")
    sys.exit(1)

print("Database connection established")

# Set up cursor
cursor = connection.cursor()

# Main Program
def main():
    option = ""
    while option.upper() != "Q":
        show_menu()
        option = get_menu_option("Select an option: ")

        if option == "1":
            print("You selected: Display all books")
            query_books()
        elif option == "2":
            print("You selected: Display a member")
            last_name = get_lastname()
            print("Searching for members with last name: " + last_name)
            query_lastname(last_name)
        elif option.upper() == "Q":
            print("Exiting program...")
        else:
            print("Invalid option. Please try again.")

# Program Execution
main()

# Close cursor
cursor.close()

# Close connection
connection.close()
