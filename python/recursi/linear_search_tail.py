#! /usr/bin/env python3 

""" 
Tail recursion when searching linearly for an element in a list.
"""

def linear_search_tail(a: list, x: int) -> int:
    """Linear search in list and return index of element in list."""
    
    n = len(a)
    if a == []:
        return -1
    elif a[n - 1] == x:
        return n - 1
    else:
        return linear_search_tail(a[:n - 1], x)
    
