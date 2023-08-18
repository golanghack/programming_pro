#! /usr/bin/env python3 

"""SUMM first n natural numbers
>>> from summ_first_n_nature_numbers import summ_first_naturals
>>> print(summ_first_naturals(3))
6
"""

def summ_first_naturals(n: int) -> int:
    """Return summ naturals."""
    
    if n != 1:
        return summ_first_naturals(n - 1) + n #recursi
    return 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()