#! /usr/bin/env python3 

import weakref

class SuperObject:
    
    def __del__(self):
        print(f'(Deleting {self}')
        
def on_finalize(*args):
    print(f'on_finalize({args!r})')
    
obj = SuperObject()
weakref.finalize(obj, on_finalize, 'extra arg')
del obj