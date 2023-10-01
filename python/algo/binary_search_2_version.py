#! /usr/bin/env python3 
import typing


def binary_search(sequence: typing.List[int], target: int) -> bool:
    """Binary search in sorted massive""" 

    start = 0 
    end = len(sequence) - 1

    while start <= end:
        middle = (start + end) // 2

        if target < sequence[middle]:
            end = middle - 1
        elif target > sequence[middle]:
            start = middle + 1
        else:
            return True
    return False

