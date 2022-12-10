#! /usr/bin/env python3 

"""<--BINARY SARCH ALGO-->"""

import math 

sorted_lst = [1, 2, 3, 4, 5]


def binary_search(sorted_lst, looking_for) -> int:
    target = math.floor(len(sorted_lst) / 2)
    max_length = len(sorted_lst)
    min_lenght = 0
    while (abs(sorted_lst[target] - looking_for) > 0.0001):
        if (sorted_lst[target] > looking_for):
            max_length = target
            target = math.floor((target + min_lenght) / 2)
        if (sorted_lst[target] < looking_for):
            min_lenght = target
            target = math.floor((target + max_length) / 2)
    return target


if __name__ == '__main__':
    print(binary_search(sorted_lst, 1))


