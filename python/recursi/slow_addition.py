#! /usr/bin/env python3 

""" 
Slow addition of two non-negative integers.
"""

def slow_addition(a: int, b: int) -> int:
    """Slow addition function."""
    
    if a == 0:
        return b 
    elif b == 0:
        return a
    else:
        return slow_addition(a - 1, b) + 1
    
