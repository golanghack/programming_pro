#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--FUZZY BOOL CLASS-->"""

"""
Implements an immutable FuzzyBool data type that can only have values in
the interval [0.0, 1.0] and which supports the basic logical operations
not (~), and (&), and or (|) using fuzzy logic.

>>> f = FuzzyBool()
>>> g = FuzzyBool(.5)
>>> h = FuzzyBool(3.75)
>>> f, g, h
(FuzzyBool(0.0), FuzzyBool(0.5), FuzzyBool(0.0))
>>> h = ~h
>>> print(f, g, h)
0.0 0.5 1.0
>>> f = FuzzyBool(0.2)
>>> f < g
True
>>> h >= g
True
>>> f + g
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'FuzzyBool' and 'FuzzyBool'
>>> int(h), int(g)
(1, 0)
>>> d = {f : 1, g : 2, h : 3}
>>> d[g]
2
"""

