#! /usr/bin/env python3 

import gc 
import weakref

class SuperObject:
    
    def __del__(self):
        print(f'(Deleting {self})')
        
def on_finalize(*args):
    print(f'on_finalize({args})')
    
obj = SuperObject()
obj_id = id(obj)

f = weakref.finalize(obj, on_finalize, obj)
f.atexit = False

del obj 

for garbage in gc.get_objects():
    if id(garbage) == obj_id:
        print('found uncollected object in gc')