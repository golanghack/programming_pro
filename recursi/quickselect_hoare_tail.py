#! /usr/bin/env python3 
from hoar import partition_hoare

def quickselect(a: list, lower:int, upper:int, k: int) -> int:
    """Select element in list with Hoare select algorithm."""
    
    if lower == upper:
        return a[lower]
    else:
        pivot_index = partition_hoare(a, lower, upper)
        if pivot_index == k - 1:
            return a[pivot_index]
        elif pivot_index < k - 1:
            return quickselect(a, pivot_index + 1, upper, k)
        else:
            return quickselect(a, lower, pivot_index - 1, k)
        