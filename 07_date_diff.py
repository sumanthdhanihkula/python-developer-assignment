"""
Problem 7: Date Difference Calculator

Write a Python program to calculate the number of days between two dates provided by the user.

Scenario:
A user wants to find how many days they've lived by inputting their birthdate and today’s date.

Approach:
- Parse input strings in dd-mm-yyyy format into datetime objects.
- Subtract to find the difference in days.
- Handle date format errors with try-except.
"""

from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, "%d-%m-%Y")
        date2 = datetime.strptime(date2_str, "%d-%m-%Y")
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        return "Invalid date format. Please use dd-mm-yyyy."

# Example usage
birthdate = input("Enter your birthdate (dd-mm-yyyy): ")
today = input("Enter today's date (dd-mm-yyyy): ")

result = calculate_date_difference(birthdate, today)
print(f"\nYou have lived for {result} days." if isinstance(result, int) else result)
