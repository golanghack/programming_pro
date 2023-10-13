#! /usr/bin/env python3 

class AllFigures:
    """Superclass for classes in Figures module."""
    
    def __init__(self, sides: int, points: set, radius: float=None) -> None:
        self._sides = sides 
        self._points = list(points)
        self._radius = radius
        if len(self._points) != self._sides:
            raise ValueError('Incorrect number of points.')
    
    def sides(self) -> int:
        return self._sides 
    
    def radius(self) -> float:
        return self._radius
    
      