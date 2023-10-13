#! /usr/bin/env python3 

from operator import * 

a = [1, 2, 3]
b = ['a', 'b', 'c']

print('a = ', a)
print('b = ', b)

print('\nConstructive\n')
print('concat(a, b) -> ', concat(a, b))

print('\nSearching\n')
print('contains(a, 1) ->', contains(a, 1))
print('contains(a, "d") -> ', contains(a, "d"))
print('countOf(a, 1) -> ', countOf(a, 1))
print('indexOf(a, 5) -> ', indexOf(a, 1))

print('\nAccess Items ->\n')
print('getitem(b, 1) -> ', getitem(b, 1))
print('getitem(b, slice(1, 3)) -> ', getitem(b, slice(1, 3)))
print('setitem(b, 1, "d") -> ', setitem(b, 1, "d"))
print(b)
print('setitem(a, slice(1, 3), [4, 5]) -> ', end=' ' )
setitem(a, slice(1, 3), [4, 5])
print(a)

print('\nDestructure -> \n')
print('delitem(b, 1) -> ', delitem(b, 1), end=' ')
print(b)
print('delitem(a, slice(1, 3)) -> ', delitem(a, slice(1, 3)), end=' ')
print(a)