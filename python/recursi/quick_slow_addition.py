#! /usr/bin/env python3 

""" 
Accelerated slow addition of two non-negative integers
numbers.
"""
def quicker_slow_addition(a: int, b: int) -> int:
    """Quick addition."""
    
    if a == 0:
        return b 
    elif b == 0:
        return a
    elif a < b:
        return quicker_slow_addition(a - 1, b) + 1
    else:
        return quicker_slow_addition(a, b - 1) + 1
    
