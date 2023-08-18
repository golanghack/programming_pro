#! /usr/bin/env python3 

def power(x: int, n: int) -> int:
    """Compute the value x**n for integer n"""

    if n == 0:
        return 1
    return x * power(x, n - 1)
