#! /usr/bin/env python3 

""" 
Calculating the sum of the digits of a non-negative integer.

>>> print(add_digits(3))
3
>>> print(add_digits(111))
3
"""

def add_digits(n: int) -> int:
    if n >= 10:
        return add_digits(n // 10) + (n % 10)
    return n 

if __name__ == '__main__':
    import doctest
    doctest.testmod()