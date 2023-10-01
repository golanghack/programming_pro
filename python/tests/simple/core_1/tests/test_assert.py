#! /usr/bin/env python3 

from math import sqrt
from pytest import approx

def magnitude(x: int, y: int) -> int:
    """Return magnitude x and y."""
    
    return sqrt((x * x) + (y * y))


assert magnitude(2, 2) == approx(2, 2)
