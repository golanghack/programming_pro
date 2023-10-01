#! /usr/bin/env python3 

""" Power function for non-negative powers
with logarithmic execution time.
"""

def power_logarithmic(b: int, n: int) -> int:
    """Power logarithmic function."""
    
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_logarithmic(b, n // 2) ** 2
    else:
        return b * (power_logarithmic(b, (n - 1) // 2) ** 2)
    