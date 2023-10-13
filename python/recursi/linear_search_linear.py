#! /usr/bin/env python3

""" 
Linear-recursive linear search for an element in a list.
"""

def linear_search_linear(a: list, x: int, n: int) -> int:
    """Return index of element in list."""
    
    if a == []:
        return -n - 1
    elif a[0] == x:
        return 0
    else:
        1 + linear_search_linear(a[1:], x, n)
        
def linear_search_linear_wrapper(a: list, x: int) -> None:
    """Wrapper."""
    
    return linear_search_linear(a, x, len(a))

