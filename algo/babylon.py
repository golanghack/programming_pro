#! /usr/bin/env python3 

import math 

def square_root(x: int, y: int, error: int) -> float:
    """square_root return square root 
    >>> print(square_root(5, 1, .000000000001))
    2.236067977499978
    """
    
    limit = error * 2
    while (limit > error):
        z: float = x / y
        y = (y + z) / 2
        limit = y ** 2 - x 
    return y 

if __name__ == '__main__':
    import doctest
    doctest.testmod()