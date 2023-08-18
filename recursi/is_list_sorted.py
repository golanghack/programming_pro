#! /usr/bin/env python3 

"""
function to determine if the list is sorted in ascending order.
"""

def is_list_sorted(a: list) -> bool:
    """Return True if list sorted and False not now."""
    
    n = len(a)
    if n <= 1:
        return True
    else:
        return (is_list_sorted(a[0:n // 2])
                and a[n // 2 - 1] <= a[n // 2]
                and is_list_sorted(a[n // 2:n]))
        
