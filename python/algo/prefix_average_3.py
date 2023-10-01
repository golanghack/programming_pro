#! /usr/bin/env python3 

import typing

def prefix_average(sequence: typing.List[int]) -> typing.List[float]:
    """Return list such that, for all j, 
    Array[j] equals average of sequence[0], ..., sequence[j].
    """ 

    lenght = len(sequence)
    Array = [0] * lenght
    total = 0
    for j in range(lenght):
        total += sequence[j]
        Array[j] = total / (j + 1)
    return Array

