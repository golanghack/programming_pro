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

if __name__ == '__main__':
    import doctest
    doctest.testmod()