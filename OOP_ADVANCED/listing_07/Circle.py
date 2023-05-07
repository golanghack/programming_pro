#! /usr/bin/env python3 

""" 
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
from Point import Point

class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self) -> float:
        """The distance of the circle`s edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.distance_from_origin()
        5.0
        """ 

        return abs(self.distance_from_origin() - self.radius)

    def area(self) -> float:
        """The crcle`s area

        >>> circle = Circle(3)
        >>> area_circle = circle.area()
        >>> int(area_circle)
        28
        """ 

        return math.pi * (self.radius ** 2)


    def circumference(self) -> float:
        """The circle`s circumreference

        >>> circle = Circle(3)
        >>> circum = circle.circumference()
        >>> int(circum)
        18
        """ 

        return 2 * math.pi * self.radius

    
    def __eq__(self, other) -> bool:
        return self.radius == other.radius and super().__eq__(other)

    
    def __reduce__(self):
        return f'Circle({self.radius!r}, {self.x!r}, {self.y!r})'

    
    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()