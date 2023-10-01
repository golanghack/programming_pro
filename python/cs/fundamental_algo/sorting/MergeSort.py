#! /usr/bin/env python3
from typing import List

def merge_sort(massive: List[int]) -> List[int]:
    """Merge sort

    >>> massive = [3, 2, 1]
    >>> merge_sort(massive)
    [1, 2, 3]
    """ 
    
    # find len massive
    if len(massive) > 1:
        # middle of massive
        middle = len(massive) // 2
        # first element in massive
        left_elem = massive[:middle]
        # last element in massive
        right_elem = massive[middle:]
        
        # recursuve
        merge_sort(left_elem)
        merge_sort(right_elem)
        first = 0
        second = 0
        threed = 0

        while first < len(left_elem) and second < len(right_elem):
            if left_elem[first] < right_elem[second]:
                massive[threed] = left_elem[first]
                first = first + 1
            else:
                massive[threed] = right_elem[second]
                second = second + 1
            threed = threed + 1
        
        while first < len(left_elem):
            massive[threed] = left_elem[first]
            first = first + 1
            threed = threed + 1
        
        while second < len(right_elem):
            massive[threed] = right_elem[second]
            second = second + 1
            threed = threed + 1
    else:
        return massive
    return massive