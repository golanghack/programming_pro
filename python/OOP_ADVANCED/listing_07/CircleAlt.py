#! /usr/bin/env python3 


""" 
>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 4
>>> circle.x = 12
>>> circle
Circle(4, 12, 0)
>>> a_circle = Circle(4, 5, 6)
>>> b_circle = Circle(4, 5, 6)
>>> a_circle == b_circle
True
>>> a_circle == circle
False
>>> a_circle != circle
True
""" 

import math 
from PointAlt import Point


class Circle(Point):

    def __init__(self, radius: int, x: int = 0, y: int = 0) -> None:
        """A Circle 

        >>> circle = Circle(3)
        >>> circle
        Circle(3, 0, 0)
        """ 

        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self) -> float:
        """The circle`s area

        >>> circle = Circle(3)
        >>> a_circle = circle.area
        >>> int(a_circle)
        28
        """ 

        return math.pi * (self.radius ** 2)

    @property
    def edge_distance_from_origin(self) -> float:
        """The distance of the circle`s edge from the orgin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin
        3.0
        """ 

        return abs(self.distance_from_origin - self.radius)

    @property
    def circumference(self) -> float:
        """The cicle`s circumference

        >>> circle = Circle(3)
        >>> circum_circle = circle.circumference
        >>> int(circum_circle)
        18
        """ 

        return 2 * math.pi * self.radius

    
    @property
    def radius(self) -> int:
        """The circle`s radius 

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(5)
        >>> circle.radius = -1 
        Traceback (most recent call last):
        ... 
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """ 

        return self.__radius 

    @radius.setter
    def radius(self, radius: int) -> None:
        assert radius > 0, 'radius must be nonzero and non-negative'
        self.__radius = radius

    def __eq__(self, other) -> bool:
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({self.radius!r}, {self.x!r}, {self.y!r})')

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()