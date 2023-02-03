#! /usr/bin/env python3 

import functools

def do_reduce(a, b):
    print(f'do_reduce({a}, {b})')
    return a * b

data = range(1, 5)
print(data)

result = functools.reduce(do_reduce, data)

print(f'result -> {result}')