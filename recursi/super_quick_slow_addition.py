#! /usr/bin/env python3 

""" 
Accelerated slow addition of two non-negative integers
numbers.
"""

def quicker_slow_addition_alt(a: int, b: int) -> int:
    """Super quick slow addition."""
    
    if a == 0:
        return b 
    elif b == 0:
        return a
    else:
        return quicker_slow_addition_alt(a - 1, b - 1) + 1 + 1
    