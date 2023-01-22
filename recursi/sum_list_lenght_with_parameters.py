#! /usr/bin/env python3 

"""Resursi func summ elements of list a. Border into lists is two parameters 
-> lower and upper indexes in list a. 
>>> print(sum_list_limits_1([1, 2, 3, 4], 1, 3))
7
"""

#decomposition task: summ(a) => summ(a[0:n-1]), a[n-1]
def sum_list_limits_1(a: list, lower: int, upper: int) -> int:
    if lower < upper:
        return a[upper] + sum_list_limits_1(a, lower, upper - 1)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()