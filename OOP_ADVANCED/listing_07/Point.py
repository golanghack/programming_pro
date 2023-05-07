#! /usr/bin/env python3

"""
Point and Circle building classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 100
>>> str(point)
'(100, 0)'
>>> a_point = Point(55, 44)
>>> b_point = Point(55, 44)
>>> a_point == b_point
True
>>> a_point == point
False
>>> a_point != point
True

>>> circle = Circle(22)
>>> circle
Circle(22, 0, 0)
>>> circle.radius = 100
>>> circle.x = 33
>>> circle
Circle(33, 100, 0)
>>> a_circle = Circle(1, 2, 3)
>>> b_circle = Circle(1, 2, 3)
>>> a_circle == b_circle
True
>>> a_circle == circle
False
>>> a_circle != circle
True
"""

import math 


class Point:

    def __init__(self, x: int = 0, y: int = 0):
        """2D cortesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0) 
        """

        self.x = x
        self.y = y 

    def distance_from_origin(self) -> float:
        """Returns the distance of the point from the origin
        
        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """ 

        return math.hypot(self.x, self.y)

    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'({self.x!r}, {self.y!r})'


