#! /usr/bin/env python3 
"""Recursion func summ elements of list with unit parameter - list.

>>> print(sum_list_lenght_2([1, 2, 3]))
6
"""

#decomposition task: summ(a) => a[0], summ(a[1:n])
def sum_list_lenght_2(a: list) -> int:
    """Return summ elements of list."""
    
    if len(a) != 0:
        return a[0] + sum_list_lenght_2(a[1:len(a)])
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()