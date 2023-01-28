#! /usr/bin/env python3 

"""
Linear-recursive logical function that determines the presence
in a non-negative integer n of the given digit d.
"""

def contains_digit(n: int, d: int) -> bool:
    """Return True? if d in n else False."""
    
    if n < 10:
        return n == d
    else:
        return (n % 10 == d) or contains_digit(n // 10, d)
    
