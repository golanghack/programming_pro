#! /usr/bin/env python3 

import typing

def prefix_average(sequence: typing.List[int]) -> typing.List[float]:
    """Return list such that, for all j, 
    zero_array[j] equals average of sequence[0], ..., sequence[j]
    """ 

    lenght = len(sequence)
    zero_array = [0] * lenght 
    for j in range(lenght):
        zero_array[j] = sum(sequence[0:j+1]) / (j + 1)
    return zero_array
