"""
Problem 2: Text Analysis with Constraints

Write a Python program to:
- Count the frequency of each word in a large paragraph, ignoring common stop words.
- Efficiently allow queries like: "Return the top N most frequent words starting with a given prefix".

Approach:
- Normalize text (lowercase, remove punctuation).
- Use a set of stop words to filter common words.
- Use a dictionary (hash map) to store word frequencies.
- For prefix queries, use list comprehension with sorting based on frequency.
"""

import string
from collections import defaultdict, Counter

# Define stop words
STOP_WORDS = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'to', 'of', 'with', 'for', 'from'}

def preprocess_text(text):
    # Remove punctuation and lowercase the text
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return [word for word in words if word not in STOP_WORDS]

def get_word_frequencies(words):
    return Counter(words)

def query_frequent_words(word_freq, prefix, top_n):
    filtered = [(word, count) for word, count in word_freq.items() if word.startswith(prefix)]
    sorted_filtered = sorted(filtered, key=lambda x: x[1], reverse=True)
    return sorted_filtered[:top_n]

# Example Usage
paragraph = """
The theory of thermodynamics is a fundamental part of physics. The third law of thermodynamics states that the entropy of a system approaches a constant minimum as the temperature approaches absolute zero.
"""

words = preprocess_text(paragraph)
frequencies = get_word_frequencies(words)

# Query Example
prefix_query = 'th'
top_n = 3
result = query_frequent_words(frequencies, prefix_query, top_n)

print(f"Top {top_n} most frequent words starting with '{prefix_query}':")
for word, count in result:
    print(f"{word}: {count}")
