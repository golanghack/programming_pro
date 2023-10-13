#! /usr/bin/env python3 

from operator import * 

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']

print('\nData\n')
print('a ', a)
print('b ', b)
print('c ', c)
print('d ', d)

a = iadd(a, b)
print('a = iadd(a, b) -> ', a)
print()

c = iconcat(c, d)
print('c = iconcat(c, d) -> ', c)