#! /usr/bin/env python3 

from typing import List
"""This program has illustrated a finding maximal value in list""" 

def find_max(data_list: List[int]) -> int:
    """Return value maximum in data_list""" 

    # The initial value to beat
    biggest = data_list[0]
    # For loop each value
    for value in data_list:
        if value > biggest:
            biggest = value
    return biggest

print(find_max([0, 2, 3]))
