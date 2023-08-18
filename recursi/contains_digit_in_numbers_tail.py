#! /usr/bin/env python3 

""" 
A tail recursive boolean function that determines whether
whether a non-negative integer n contains a digit d.
"""

def contains_digit_tail(n: int, d: int) -> bool:
    """Return True for d in n else False."""
    
    if n < 10:
        return n == d 
    elif n % 10 == d:
        return True
    else:
        return contains_digit_tail(n // 10, d)
    
