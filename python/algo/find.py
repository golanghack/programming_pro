#! /usr/bin/env python3 
from typing import List
def find(sequence: List[int], value: int) -> int:
    """Return index j such that seqience[j] == value, or -1 if no such elem"""

    lenght = len(sequence)
    j = 0
    while j < lenght:
        if sequence[j] == value:
            return j 
        j += 1
    return -1 

