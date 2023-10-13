#! /usr/bin/env python3 

"""MERGE SORT LIST."""

def merge_sort(a: list) -> list:
    """Merge sort algo."""
    
    n = len(a)
    if n <= 1:
        return a
    else:
        a_one = merge_sort(a[0:n // 2])
        a_two = merge_sort(a[n // 2:n])
        return merge(a_one, a_two)
    
# list and list b are sorted in asceding order
def merge(a: list, b: list) -> list:
    """Merging lists."""
    
    if a == []:
        return b 
    elif b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])
        
print(merge_sort([2, 4, 2, 1, 8]))