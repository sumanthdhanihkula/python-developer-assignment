"""
Problem 1: Seating Arrangement Problem

You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd like to sit next to.
The goal is to determine a valid circular seating arrangement satisfying all preferences.

Approach:
- This is a constraint satisfaction problem where each guest must be seated next to their two preferred neighbors.
- We'll generate all possible circular permutations of the guests and check each one to see if it satisfies all neighbor preferences.
- If any arrangement satisfies all constraints, we return it. Otherwise, we state that no valid arrangement is possible.
"""

from itertools import permutations

def is_valid_arrangement(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left_neighbor = arrangement[(i - 1) % n]
        right_neighbor = arrangement[(i + 1) % n]
        if not (left_neighbor in preferences[guest] and right_neighbor in preferences[guest]):
            return False
    return True

def find_seating_arrangement(preferences):
    guests = list(preferences.keys())
    for perm in permutations(guests):
        if is_valid_arrangement(perm, preferences):
            return list(perm)
    return None

# Sample Input
guests_preferences = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

# Output Result
result = find_seating_arrangement(guests_preferences)
if result:
    print("Valid Seating Arrangement Found:")
    print(" -> ".join(result))
else:
    print("No valid seating arrangement is possible.")
