#! /usr/bin/env python3 

import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject:
    
    def __init__(self, value: str) -> None:
        self.value = value
        
    def __eq__(self, other: object) -> bool:
        
        print(f'---testing __eq__({self.value}, {other.value})')
        return self.value == other.value
    
    def __gt__(self, other: object) -> bool:
        
        print(f'---testing __gt__({self.value}, {other.value})')
        return self.value > other.value
    
    
print('Methods ->\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a_object = MyObject(1)
b_object = MyObject(2)

print('\nComrisions ->')
for expr in ['a < b', 'a <= b', 'a >= b', 'a > b']:
    print(f'\n{expr:<6}')
    result = eval(expr)
    print(f'---result of{expr} -> {result}')