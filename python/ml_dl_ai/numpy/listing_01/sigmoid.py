#! /usr/bin/env python3

import numpy as np
from numpy import ndarray
from into_functions import Chain
from deriv import deriv

def sigmoid(arg_x: ndarray) -> ndarray:
    """Sigmoid use for every element from ndarray"""

    return 1 / (1 + np.exp(-1))

def chain_deriv_2(chain: Chain, input_range: ndarray) -> ndarray:
    """Deriver for two included functions
        (func2(func1(x))) = func2`(func1(x)) * func1`(x) 
        with network rule
    """

    assert len(chain) == 2, 'Chain object lenght must be 2'
    assert input_range.ndim == 1, 'Range into data -> 1-r ndarray'

    func1 = chain[0]
    func2 = chain[1]

    # dfunc1 / dx
    func1_of_x = func1(input_range)

    # dfunc1/du
    dfunc1dx = deriv(func1, input_range)

    # dfunc2/du(func1(x))
    dfunc2du = deriv(func2, func1(input_range))

    # every elements multyple
    return dfunc1dx * dfunc2du

    