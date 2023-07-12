#! /usr/bin/env python3 
from typing import List

def uniq_1(sequence: List[int]) -> bool:
    """Return True if there are no duplicate elements in sequence""" 

    lenght = len(sequence)
    for j in range(lenght):
        for k in range(j + 1, len(sequence)):
            if sequence[j] == sequence[k]:
                return False
    return True

