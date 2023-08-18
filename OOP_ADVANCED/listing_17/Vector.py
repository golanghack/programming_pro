#! /usr/bin/env python3 

from math import hypot

class Vector:
    """  
    Class Vector -> imitation program interface for math vectors
    Binary vector.

    Docs tests

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2 
    Vector((4, 5))
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector((9, 12))
    >>> abs(v * 3)
    15.0
    """ 

    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y 

    def __repr__(self):
        return f'Vector({self.x, self.y})'

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: int):
        x = self.x + other.x 
        y = self.y + other.y 
        return Vector(x, y)

    def __mul__(self, scalar: int):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    

