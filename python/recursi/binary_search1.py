#! /usr/bin/env python3 

def binary_search(a: list, x: int, lower: int, upper: int) -> int:
    """Binary search."""
    
    if lower > upper: # empty
        return - 1
    else:
        middle = (lower + upper) // 2
        if x == a[middle]:
            return middle
        elif x < a[middle]:
            return binary_search(a, x, lower, middle - 1)
        else:
            return binary_search(a, x, middle + 1, upper)
        
