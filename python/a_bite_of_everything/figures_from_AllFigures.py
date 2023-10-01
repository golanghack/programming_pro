#! /usr/bin/env python3 

from AllFigures import AllFigures

class Triangle(AllFigures):
    """Subclass from AllFigures superclass."""
    
    def __init__(self, points: set) -> None:
        AllFigures.__init__(self, 3, points, radius=None)
        
    def __str__(self) -> str:
        return 'Trinagle.'
    
class Square(AllFigures):
    """Subclass from AllFigures superclass."""
    
    def __init__(self, points: set) -> None:
        AllFigures.__init__(self, 4, points, radius=None)
        
    def __str__(self) -> str:
        return 'Square.'
    
class Circle(AllFigures):
    """Subclass from AllFigures superclass."""
    
    def __init__(self, points: set, radius: float) -> None:
        AllFigures.__init__(self, 2, points, radius)
        
    def __str__(self) -> str:
        return 'Circle.'