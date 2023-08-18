#! /usr/bin/env python3 

"""Recursion func summ elements of list with unit parameter - list.

>>> print(sum_list_lenght_1([1, 2, 3]))
6
"""

#decomposition of task -> summ(a) => summ(a[0:n-1]), a[n-1]
def sum_list_lenght_1(a: list) -> int:
    """Return summ elements of list a."""
    
    if len(a) != 0:
        return (sum_list_lenght_1(a[0:len(a) - 1]) + a[len(a) - 1])
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()