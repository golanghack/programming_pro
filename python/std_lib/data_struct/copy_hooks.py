#! /usr/bin/env python3 

import copy
import functools

@functools.total_ordering
class MyClass:
    
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other) -> bool:
        return self.name == other.name 
    
    def __gt__(self, other) -> bool:
        return self.name > other.name
    
    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)
    
    def __deepcopy__(self, memo):
        print(f'__deepcopy__({memo})')
        return MyClass(copy.deepcopy(self.name, memo))
    
a = MyClass('a')

s_copy = copy.copy(a)
d_copy = copy.deepcopy(a)