#! /usr/bin/env python3 

import functools

@functools.singledispatch
def my_func(arg):
    print(f'default my_func({arg})')
    
@my_func.register(int)
def my_func_int(arg):
    print(f'my_func_int({arg})')
    
@my_func.register(list)
def my_func_list(arg):
    print('my_func_list()')
    for item in arg:
        print(f'{item}')
        
my_func('string argument')
my_func(1)
my_func(1.1)
my_func(['a', 'b', 'c'])
    