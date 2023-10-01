#! /usr/bin/env python3 

def binary_search_iterative(data: list, target: int) -> bool:
    """Return True is target found in the list"""

    low = 0 
    hight = len(data) - 1

    while low <= hight:
        middle = (low + hight) // 2

        if target == data[middle]:
            return True
        elif target < data[middle]:
            hight = middle - 1
        else:
            low = middle + 1
    return False

