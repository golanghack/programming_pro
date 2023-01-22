#! /usr/bin/env python3 
"""Recursion func summ elements of list with unit parameter - list.

>>> print(sum_list_lenght_3([1, 2, 3]))
6
"""

#decomposition task: summ(a) => summ(a[0:n//2]), summ(a[n//2:n])
def sum_list_lenght_3(a: list) -> int:
    """Return summ elements of list."""
    
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        middle = len(a) // 2
        return (sum_list_lenght_3(a[0:middle]) + sum_list_lenght_3(a[middle:len(a)]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()