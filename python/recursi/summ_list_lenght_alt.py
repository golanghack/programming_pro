#! /usr/bin/env python3 
"""Recursion func summ elements of list with unit parameter - list.

>>> print(sum_list_lenght_alt([1, 2, 3]))
6
"""

#decomposition task: summ(a) => a[0], summ(a[1:n])
def sum_list_lenght_alt(a: list) -> int:
    """Return summ elements of list."""
    
    if a != []:
        return a[0] + sum_list_lenght_alt(a[1:])
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()