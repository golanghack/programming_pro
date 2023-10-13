#! /usr/bin/env python3 

import functools

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass

@functools.singledispatch
def my_func(arg):
    print(f'default my_func({arg.__class__.__name__})')
    
@my_func.register(A)
def my_func_A(arg):
    print(f'my_func_A({arg.__class__.__name__})')
    
@my_func.register(B)
def my_func_B(arg):
    print(f'my_func_B({arg.__class__.__name__})')
    
@my_func.register(C)
def my_func_C(arg):
    print(f'my_func_C({arg.__class__.__name__})')

my_func(A())
my_func(B())
my_func(C())
my_func(D())
my_func(E())
