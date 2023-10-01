#! /usr/bin/env python3
from typing import List

def insertion_sort(massive: List[int]) -> List[int]:
    """Insertion sorting
    
    >>> massive = [2, 3, 1]
    >>> insertion_sort(massive)
    [1, 2, 3]
    """
    
    # loop all elements
    for i in range(1, len(massive)):
        # remove
        base = i - 1
        # next
        next_elem = massive[i]
        while (massive[base] > next_elem) and (base >= 0):
            # current elem with next elem 
            massive[base + 1] = massive[base]
            base = base - 1
        massive[base + 1] = next_elem
    return massive


