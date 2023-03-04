#! /usr/bin/env python3 

from quick_sort_in_place import partition

def quick_select(l: list, k: int):
    return _quick_select(l, k, 0, len(l))

def _quick_select(l: list, k: int, left: int, right: int):
    pivot = partition(l, left, right)
    if k <= pivot:
        return _quick_select(l, k, left, pivot)
    elif k == pivot + 1:
        return l[pivot]
    else:
        return _quick_select(l, k, pivot + 1, right)