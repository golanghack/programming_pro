#! /usr/bin/env python3 

"""<--INVERSE SINUS-->"""

import math 

#binary_search function
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


def inverse_sinus(number):
    """This function find position number sinus mean in position"""
    #pos -> position
    pos = [x * math.pi / 10000 - math.pi / 2 for x in list(range(0, 10000))]
    _range = [math.sin(x) for x in pos]
    result = pos[binary_search(_range, number)]
    return result

if __name__ == '__main__':
    print(f'{inverse_sinus(0.9):.2f}')