#! /usr/bin/env python3 

def power(x: int, n: int) -> int:
    """Compute the value x**n fo integer x""" 

    if n == 0:
        return 1
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x 
    return result

print(power(9, 2))