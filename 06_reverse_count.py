"""
Problem 6: Reverse Counting (Recursion Check)

Print numbers from 1000 down to 1 using recursion.
Restrictions: No loops (for, while) and no built-in range() function.

Approach:
- Use a recursive function that prints the number and calls itself with number - 1 until 1 is reached.
"""

def reverse_count(n):
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)

# Start the countdown
reverse_count(1000)
