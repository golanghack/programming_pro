#! /usr/bin/env python3

import math

def to_fraction(x: float, y: float, length: int) -> float:
    """to_fraction return dont wrap fraction
    >>> print(to_fraction(105, 33, 10))
    [3, 5, 2]
    """
    
    output: list = []
    big: float = max(x, y)
    small: float = min(x, y)
    while small > 0 and len(output) < length:
        quotient: int = math.floor(big / small)
        output.append(quotient)
        new_small: float = big % small
        big = small
        small = new_small
    return output

def to_number(fraction: float) -> int:
    """to_number return number from fraction
    >>> print(to_number([3, 5, 2]))
    3.1818181818181817
    """
    
    index: int = -1
    number: int = fraction[index]
    
    while abs(index) < len(fraction):
        next_: int = fraction[index - 1]
        number = 1 / number + next_ 
        index -= 1
    return number

def continue_fraction(x: float, error: float, lenght: int) -> list:
    """continue_fracton return list numbers"""
    
    output = []
    first = int(x)
    second = x - first
    output.append(first)
    while second > error and len(output) < lenght:
        next_: float = math.floor(1 / second)
        second = (1 / second) - next_
        output.append(next_)
        second = abs(to_number(output) - x)
    return output
print(continue_fraction(1.4142135623730951,0.00001,100))