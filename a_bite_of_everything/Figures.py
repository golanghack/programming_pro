#! /usr/bin/env python3 

class Triangle:
    """Triangle -> class of geometric figure. Illustrated is."""
    
    def __init__(self, points: set) -> None:
        self.sides = 3 
        self._points = list(points)
        if len(self._points) != 3:
            raise ValueError('The Triangle must be 3 sides!')
        
    def count_sides(self) -> int:
        return 3 
    
    def __str__(self) -> str:
        return 'Triangle'
    

class Square:
    """Square -> class of geometric figure. Illustrated is."""
    
    def __init__(self, points: set) -> None:
        self._sides = 4 
        self._points = list(points)
        if len(self._points) != 4:
            raise ValueError('The square figure must be 4 sides!')
        
    def sides(self) -> int:
        return 4
    
    def __str__(self) -> str:
        return 'Square.'
    
class Circle:
    """Circle -> class of geometric figure.Illustrated is."""
    
    def __init__(self, radius: float, points: set) -> None:
        self._center = list(points)
        self._radius = radius
        
    def radius(self) -> float:
        return self.radius
    
    def __str__(self) -> str:
        return 'Circle'