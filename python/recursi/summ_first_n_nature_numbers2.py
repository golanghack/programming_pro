#! /usr/bin/env python3


""" 
>>> print(summ_first_naturals(3))
6
"""

def summ_first_naturals(n: int) -> int:
    """Summ first n natural numbers."""
    
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n % 2:
        return (3 * summ_first_naturals((n - 1) / 2) + summ_first_naturals((n + 1) / 2))
    else:
        return (3 * summ_first_naturals((n / 2)) + summ_first_naturals((n / 2 - 1)))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    