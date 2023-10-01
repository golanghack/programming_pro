#! /usr/bin/env python3

"""Casting a non-negative integer n to base b."""

def decimal_to_base(n: int, b: int) -> int:
    """From decimal to anything base."""
    
    if n < b:
        return n 
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)
    
