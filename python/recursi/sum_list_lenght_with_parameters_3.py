#! /usr/bin/env python3 

"""Resursi func summ elements of list a. Border into lists is two parameters 
-> lower and upper indexes in list a. 
>>> print(sum_list_limits_3([1, 2, 3, 4], 1, 3))
7
"""

#decomposition task: summ(a) => summ(a[0:n//2]), summ(a[n//2:n])
def sum_list_limits_3(a: list, lower: int, upper: int) -> int:
    if lower > upper:
        return 0
    elif lower == upper:
        return a[lower] #ecvivalent -> a[upper]
    else:
        middle = (lower + upper) // 2
        return (sum_list_limits_3(a, lower, upper) + sum_list_limits_3(a, middle + 1, upper))

if __name__ == '__main__':
    import doctest
    doctest.testmod()