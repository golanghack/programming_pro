#! /usr/bin/env python3 

import math 

""" 
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 100
>>> str(point)
'(100, 0)'
>>> a_point = Point(3, 4)
>>> b_point = Point(3, 4)
>>> a_point == b_point
True
>>> a_point == point
False
>>> a_point != point
True
"""

class Point:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """ 

        self.x = x 
        self.y = y 


    @property
    def distance_from_origin(self) -> float:
        """The distance of the point from the origin 

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        """ 

        return math.hypot(self.x, self.y)

    def __eq__(self, other)-> bool:
        return self.x == other.x and self.y == other.y 

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({self.x!r}, {self.y!r})')

    def __str__(self) -> str:
        return f'({self.x!r}, {self.y!r})'

    