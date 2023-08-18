#! /usr/bin/env python3 

import weakref

class ExpensiveObject:
    
    def __del__(self):
        print(f'Deleting -> {self})')
        
def callback(reference: str) -> str:
    """Return for deleting object."""
    
    print(f'callback({reference!r})')
    
obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj -> ', obj)
print('ref -> ', r)
print('r() -> ', r())

print('deleting obj')
del obj
print('r() -> ', r())