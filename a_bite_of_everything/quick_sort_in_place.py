#! /usr/bin/env python3 

def quick(l: list,  left: int = 0, right: int = None):
    # base
    if right is None:
        right = len(l)
    if right - left > 1:
        # divide
        middle = partition(l, left, right)
        
        # conque
        quick(l, left, right)
        quick(l, middle + 1, right)
        
def partition(l: list, left: int, right: int):
    pivot = right - 1
    i = left
    j = pivot - 1
    
    while i < j:
        # moved i in position >= ;[pivot]
        while l[i] < l[pivot]:
            i = i + 1
            
        # moved j in position < l[pivot]
        while (i < j and l[j] >= l[pivot]):
            j = j - 1
        # replacing 
        if i < j:
            l[i], l[j] = l[j], l[i]
    # in place 
    if l[pivot] <= l[i]:
        l[pivot], l[i] = l[i], l[pivot]
        pivot = i
    return pivot

    