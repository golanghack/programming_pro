#! /usr/bin/env python3 

from operator import * 

class MyObject:
    """Simple class for attrgetter."""
    
    def __init__(self, arg: str) -> None:
        super().__init__()
        self.arg = arg 
        
    def __repr__(self) -> str:
        return f'MyObject({self.arg})'
    
list_of_objects = [MyObject(i) for i in range(5)]
print('objects -> ', list_of_objects)

# getting arg from every object 
from_object_get_arg = attrgetter('arg')
vals = [from_object_get_arg(i) for i in list_of_objects]
print('arg values -> ', vals)

# sorting with arg 
list_of_objects.reverse()
print('reversed -> ', list_of_objects)
print('sorted -> ', sorted(list_of_objects, key=from_object_get_arg))