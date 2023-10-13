#! /usr/bin/env python3 

from random import randrange

def quick(l: list):
    _quick(l, 0, len(l))
    
def _quick(l: list, left: int, right: int):
    if right - left > 1:
        middle = partition(l, left, right)
        _quick(l, left, middle)
        _quick(l, middle + 1, right)
        
def partition(l: list, left: int, right: int):
    pivot = randrange(left, right)
    l[pivot], l[right - 1] = l[right - 1]. l[pivot]
    i, j, pivot = left, right - 2, right - 1
    
    while i < j:
        while l[i] < l[pivot]:
            i += 1
        while i < j and l[i] >= l[pivot]:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    if l[pivot] <= l[i]:
        l[pivot], l[i] = l[i], l[pivot]
        pivot = i
    return pivot

