#! /usr/bin/env python3 

from typing import List

def binary_search(data: List[int], target: int, low: int, high: int) -> bool:
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive
    """ 

    if low > high:
        return False
    else:
        middle = (low + high) // 2 
        if target == data[middle]:
            return True
        elif target < data[middle]:
            return binary_search(data, target, low, middle - 1)
        else:
            return binary_search(data, target, middle + 1, high)