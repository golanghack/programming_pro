#! /usr/bin/env python3 

""" 
list splitter helper methods.
"""

def get_smaller_than_ro_equal_to(a: list, x: int) -> list:
    """returrn lists less origin."""
    
    if a == []:
        return []
    elif a[0] <= x:
        return [a[0]] + get_smaller_than_ro_equal_to(a[1:], x)
    else:
        return get_smaller_than_ro_equal_to(a[1:], x) 