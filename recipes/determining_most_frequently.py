#! /usr/bin/env python3

"""  
Problem 

You have a sequence of items, and you’d like to determine the most frequently occurring
items in the sequence.
""" 

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under',
]

word_counts = Counter(words)

top_five_words = word_counts.most_common(5)
print(top_five_words)