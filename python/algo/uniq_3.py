#! /usr/bin/env python3 
from typing import List

def unique_3(sequence: List[int], start: int, stop: int) -> bool:
    """Return True is threse are no duplicates elements
         in slice sequence[start: stop]
    """

    if stop - start <= 1: 
        return True
    elif not unique_3(sequence, start, stop-1):
        return False
    elif not unique_3(sequence, start+1, stop):
        return False
    else:
        return sequence[start] != sequence[stop - 1]



