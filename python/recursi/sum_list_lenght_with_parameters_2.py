#! /usr/bin/env python3 

"""Resursi func summ elements of list a. Border into lists is two parameters 
-> lower and upper indexes in list a. 
>>> print(sum_list_limits_2([1, 2, 3, 4], 1, 3))
5
"""

#decomposition task: summ(a) => a[0], summ(a[1:n])
def sum_list_limits_2(a: list, lower: int, upper: int) -> int:
    if lower < upper:
        return a[lower] + sum_list_limits_2(a, lower + 1, upper)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()