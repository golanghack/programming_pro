#! /usr/bin/env python3 

def get_greater_than(a: list, x: int) -> list:
    """Return greater elements in list."""
    
    if a == []:
        return []
    elif a[0] > x:
        return [a[0]] + get_greater_than(a[1:], x)
    else:
        return get_greater_than(a[1:], x)
