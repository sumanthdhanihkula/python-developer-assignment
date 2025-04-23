"""
Problem 10: Solve in Fewest Steps
---------------------------------
Given a string containing letters and digits, separate and sort the letters and digits individually.
Return a concatenated string with sorted letters first, followed by sorted digits.

Approach:
1. Separate characters using isalpha() and isdigit().
2. Sort each list.
3. Concatenate the results and return.
"""

def sort_letters_digits(s: str) -> str:
    letters = sorted([ch for ch in s if ch.isalpha()])
    digits = sorted([ch for ch in s if ch.isdigit()])
    return ''.join(letters + digits)

# Example usage:
if __name__ == "__main__":
    input_str = "B4A1D3"
    result = sort_letters_digits(input_str)
    print(result)  # Output: ABD134
