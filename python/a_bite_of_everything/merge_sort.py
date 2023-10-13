#! /usr/bin/env python3 

def merge_sort(l: list):
    # base 
    if len(l) < 2:
        return
    
    # dividing 
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    
    # concuer
    merge_sort(left)
    merge_sort(right)
    
    # merging 
    merge(left, right, l)
    
def merge(left: list, right: list, l: list) -> None:
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l[i + j] = left[i]
            i = i + 1
        else:
            l[i + j] = right[j]
            j = j + 1
    l[i + j:] = left[i:] + right[j:]
    
    
            
 
    
