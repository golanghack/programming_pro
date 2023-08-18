#! /usr/bin/env python3 

""" 
TASK

Is a List already in Sorted Order?
(41 Lines)
Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted
"""

from typing import List

def is_sorted(input_list: List[int]) -> bool:
    """Return True if sorted and False another""" 

    if input_list == []:
        return True
    elif len(input_list) == 1:
        return True
    elif len(input_list) == 2:
        return True
    else:
        if input_list[0] < input_list[1] and input_list[1] < input_list[2]:
            return True
        elif input_list[0] > input_list[1] and input_list[1] > input_list[2]:
            return True
        else:
            return False
my_list = [1, 2, 3, 33]
print(is_sorted(my_list))