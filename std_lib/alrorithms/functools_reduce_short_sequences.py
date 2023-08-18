#! /usr/bin/env python3 

import functools

def do_reduce(a, b):
    print(f'do_reduce({a},{b})')
    return a * b

print('Single item in sequence with initializer -> ', functools.reduce(do_reduce, [1], 99))

print('Emty sequence with initializer -> ', functools.reduce(do_reduce, [], 99))

try:
    print('Empty sequence -> ', functools.reduce(do_reduce, []))
except TypeError as err:
    print(f'!!!ERROR!!! -> {err}')