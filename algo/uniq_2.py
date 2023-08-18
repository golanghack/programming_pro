#! /usr/bin/env python3 
from typing import List

def uniq_2(sequence: List[int]) -> bool:
    """Return True is there are no duplicate elements in sequence""" 

    temp: List[int] = sorted(sequence)
    lenght: int = len(temp)
    for element in range(1, lenght):
        if sequence[element - 1] == sequence[element]:
            return False
    return True

    