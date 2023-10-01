#! /usr/bin/env python3 

import functools
from typing import Dict

def map_frequency(text: str) -> Dict[str, int]:
    """Mapping function for dataset."""
    
    words = text.split(' ')
    frequences = {}
    for word in words:
        if word in frequences:
            # add 1 to counter if word in frequences
            frequences[word] = frequences[word] + 1
        else:
            # if word dont have in frequences
            frequences[word] = 1
    return frequences

def reducing(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            # if word in both dicts added counter
            merged[key] = merged[key] + second[key]
        else:
            # if word dont have in dict -> copy counter
            merged[key] = second[key]
    return merged

lines = [
    'aaaaa aaaa aaa', 
    'aaaaa aaaa aaa', 
    'bbb bbb bbb bbb', 
    'ddd ddd bbb bbb',
]

mapped_results = [map_frequency(line) for line in lines]

for result in mapped_results:
    print(result)
    
# reduction
print('final results -> ', functools.reduce(reducing, mapped_results))
    
    