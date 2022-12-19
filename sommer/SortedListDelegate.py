#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SORTED LISR DELEGATE -> Illustrated by decoration of classes-->
>>> L = SortedList((5, 8, -1, 3, 4, 22))
>>> L[2] = 18 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TypeError: use add() to insert a value and rely on the...
>>> list(L)
[-1, 3, 4, 5, 8, 22]
>>> L.add(5)
>>> L.add(5)
>>> L.add(6)
>>> list(L)
[-1, 3, 4, 5, 5, 5, 6, 8, 22]
>>> L.index(4)
2
>>> L.count(5), L.count(2)
(3, 0)
>>> L.insert(2, 9)
Traceback (most recent call last):
...
AttributeError: 'SortedList' object has no attribute 'insert'
>>> L.reverse()
Traceback (most recent call last):
...
AttributeError: 'SortedList' object has no attribute 'reverse'
>>> L.sort()
Traceback (most recent call last):
...
AttributeError: 'SortedList' object has no attribute 'sort'

>>> L = SortedList([9, -5, 3, -7, 8, 14, 0, 8, 3])
>>> print(L)
[-7, -5, 0, 3, 3, 8, 8, 9, 14]
>>> del L[0]
>>> del L[-1]
>>> del L[5]
>>> print(L)
[-5, 0, 3, 3, 8, 9]
>>> del L[25]
Traceback (most recent call last):
...
IndexError: list assignment index out of range
>>> del L[-3:]
>>> print(L)
[-5, 0, 3]

>>> L = SortedList([9, -5, 3, -7, 8, 14, 0, 8, 3])
>>> L[0], L[3], L[4], L[-1]
(-7, 3, 3, 14)
>>> L[15]
Traceback (most recent call last):
...
IndexError: list index out of range
>>> L[:3]
[-7, -5, 0]
>>> L[4:8]
[3, 8, 8, 9]

>>> L = SortedList([5, 5, -18, -1, 3, 4, 7, 8, 22, 99, 2, 1, 3])
>>> result = []
>>> for x in L:
...     result.append(x)
>>> print(result)
[-18, -1, 1, 2, 3, 3, 4, 5, 5, 7, 8, 22, 99]

>>> L = SortedList([5, 5, -18, -1, 3, 4, 7, 8, 22, 99, 2, 1, 3])
>>> len(L)
13
>>> L = SortedList()
>>> len(L)
0

>>> L = SortedList([-1, 3, 4, 7, 8, 22, -9, 2, 1, 3])
>>> str(L)
'[-9, -1, 1, 2, 3, 3, 4, 7, 8, 22]'
>>> L = SortedList()
>>> str(L)
'[]'
>>> L = SortedList(("the", "quick", "brown", "fox", "jumped"))
>>> str(L)
"['brown', 'fox', 'jumped', 'quick', 'the']"

>>> L = SortedList([-18, -1, 3, 4, 5, 5, 7, 8, 22, 99])
>>> print(L)
[-18, -1, 3, 4, 5, 5, 7, 8, 22, 99]
>>> L.pop()
99
>>> L.pop(0)
-18
>>> L.pop(5)
7
>>> print(L)
[-1, 3, 4, 5, 5, 8, 22]
>>> print(list(reversed(L)))
[22, 8, 5, 5, 4, 3, -1]
>>> L.pop(12)
Traceback (most recent call last):
...
IndexError: pop index out of range
"""

import Util