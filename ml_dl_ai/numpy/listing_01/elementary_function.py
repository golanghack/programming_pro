#! /usr/bin/env python3

"""Elementary function"""

import numpy as np 
from numpy import ndarray

def square(x: np.ndarray) -> ndarray:
    """Return x ** 2""" 

    return np.power(x, 2)

def leajky_relu(x: ndarray) -> ndarray:
    """RELU function for element of ndarray"""
    
    return np.maximum(0.2 * x, x)
