#! /usr/bin/env python3 

from operator import * 

class MyObject:
    """Operator overload."""
    
    def __init__(self, val: str) -> None:
        super(MyObject, self).__init__()
        self.val = val
        
    def __str__(self) -> str:
        return f'MyObject({self.val})'
    
    def __lt__(self, other: str) -> None:
        """Less when."""
        
        print(f'Testing {self} < {other}')
        return self.val < other.val
    
    def __add__(self, other):
        """Summ."""
        
        print(f'Adding {self} + {other}')
        return MyObject(self.val + other.val)
    
object_one = MyObject(1)
object_two = MyObject(2)

print('Comparison -> ')
print(lt(object_one, object_two))

print('\nArithmetic -> ')
print(add(object_one, object_two))