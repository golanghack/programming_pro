#! /usr/bin/env python3 

import weakref

class ExpensiveObject:
    
    def __del__(self):
        print(f'(Deleting -> {self})')
        
obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj -> ', obj)
print('ref -> ', r)
print('r() -> ', r())
print('deleting obj')
del obj
print('r() -> ', r())