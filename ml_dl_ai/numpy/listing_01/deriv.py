#! /usr/bin/env python3 

from numpy import ndarray
from typing import Callable

def deriv(func: Callable[[ndarray], ndarray], 
            input_: ndarray, 
            delta: float=0.001) -> ndarray:
    """dirivision for function `func` on every element massive `input_`"""

    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)

