#! /usr/bin/env python3 

from operator import * 

a = 1
b = 5.0

print('a = ', a)
print('b = ', b)

for func in (lt, le, eq, ne, ge, gt):
    print(f'{func.__name__}(a, b) -> {func(a, b)}')