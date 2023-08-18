#! /usr/bine/vn python3 

from quick_sort_in_place import partition

def quick_select(l: list, k: int):
    left, right = 0, len(l)
    while left < right:
        pivot  = partition(l, left, right)
        if k <= pivot:
            right = pivot
        elif k == pivot + 1:
            return l[pivot]
        else:
            left = pivot + 1
    return l[left]
    
    