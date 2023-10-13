#! /usr/bin/env python3 

import functools

def standalone(self, a: int=1, b: int=2) -> None:
    """Independent function."""
    
    print('---called standalone with -> ', (self, a, b))
    if self is not None:
        print('---self.attr -> ', self.attr)
        
class MyClass:
    """Demonstration class for functools."""
    
    def __init__(self) -> None:
        self.attr = 'instance attribute'
        
    method_one = functools.partialmethod(standalone)
    method_two = functools.partial(standalone)
    
obj = MyClass()

print('standalone')
standalone(None)
print()

print('method_one as partialmethod')
obj.method_one()
print()

print('mthod_two as partial.')
try:
    obj.method_two()
except TypeError as err:
    print(f'!!!ERROR!!! -> {err}')