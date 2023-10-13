#! /usr/bin/env python3 

from numpy import ndarray
from typing import List, Callable

# Function -> into ndarray and output ndarray
Array_Function = Callable[[ndarray], ndarray]

# list of functions
Chain = List[Array_Function]

def chan_len_2(chain: Chain, arr: ndarray) -> ndarray:
    """Find two function in chain object"""

    assert len(chain) == 2, 'Lenght of object must be 2'

    func1 = chain[0]
    func2 = chain[1]

    return func2(func1(arr))