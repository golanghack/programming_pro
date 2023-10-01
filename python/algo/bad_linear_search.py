#! /usr/bin/env python3 

def bad_linear_search(input_list: list, element: int) -> int:
    for index, value in enumerate(input_list):
        if value == element:
            return index
    return -1 


