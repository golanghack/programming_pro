#! /usr/bin/env python3 

import weakref

class SuperObject:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def __del__(self):
        print(f'(Deleting {self})')
        
obj = SuperObject('My Object')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj -> ', obj.name)
print('via ref -> ', r().name)
print('via proxy -> ', p.name)
del obj

print('via proxy -> ', p.name)