#! /usr/bin/env python3
from typing import List

def bubble_sort(massive: List[int]) -> List[int]:
    """Bubble sort algo
    
    >>> massive = [6, 5, 8, 3, 1]
    >>> bubble_sort(massive)
    [1, 3, 5, 6, 8]
    """
    # find last element
    last_elem = len(massive) - 1
    # move bigger in end
    for passed in range(last_elem, 0, -1):
        # replaced
        for idx in range(passed):
            if massive[idx] > massive[idx + 1]:
                massive[idx], massive[idx + 1] = massive[idx + 1], massive[idx]
    return massive

if __name__ == '__main__':
    import doctest
    doctest.testmod()