#! /usr/bin/env python3 

""" 
Vector2d.py -> simpless class for demo special methods.

In class don`t have a exceptions.

addition -> 
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)

abs -> 
>>> v = Vector(3, 4)
>>> abs(v)
5.0 

multiple on number (scalar) -> 
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0 
""" 

import math

class Vector:
    """Vector simple class 

    x -> coords, int 
    y -> coords, int
    """ 

    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x 
        self.y = y 

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: int):
        x = self.x + other.x 
        y = self.y + other.y 
        return Vector(x, y)

    def __mul__(self, numder: int):
        return Vector(self.x * numder, self.y * numder)

    
