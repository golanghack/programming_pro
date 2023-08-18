#! /usr/bin/env python3 

def search(target: int, stack: list) -> int:
    """Search(binary) target int in stack list"""

    start: int = 0 
    end: int = len(stack) - 1

    while start <= end:
        middle = start + (end - start) // 2
        middle_element = stack[middle]
        if middle_element == target:
            return middle
        elif middle_element < target:
            start = middle + 1
        else:
            end = middle - 1

    raise ValueError('Target not in stack')