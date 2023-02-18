#! /usr/bin/env python3 

class Vector:
    """This class implementing of all work with vectors.
    
    >>> first = Vector(3, 4)
    >>> print(first.normalizer())
    5.0
    >>> print(Vector(5, 12).normalizer())
    13.0
    """
    
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y 
        
    def normalizer(self) -> set:
        """Return norm vectors."""
        
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()