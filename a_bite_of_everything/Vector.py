#! /usr/bin/env python3 

class Vector:
    """This class implementing of all work with vectors.
    
    >>> first = Vector(3, 4)
    >>> print(first.normalizer())
    5.0
    >>> print(Vector(5, 12).normalizer())
    13.0
    >>> new_one = Vector(3, 4)
    >>> new_two = Vector(3, 6)
    >>> print(new_one + new_two)
    (6.00, 10.00)
    """
    
    def __init__(self, x, y) -> None:
        try:
            self.x = float(x) 
            self.y = float(y)
        except ValueError:
            self.x = 0.0 
            self.y = 0.0 
        
    def normalizer(self) -> set:
        """Return norm vectors."""
        
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __add__(self, other):
        """Return new Vector."""
        
        new_vector_x = self.x + other.x 
        new_vector_y = self.y + other.y
        
        return Vector(new_vector_x, new_vector_y)
    
    def __str__(self) -> str:
        return f'({self.x:.2f}, {self.y:.2f})'
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()