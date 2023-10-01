#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--QUADRATIC-->"""

import cmath
import math 
import sys 

def get_float(msg, allow_zero):
    """get_float is function return float from user."""
    
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
        except ValueError as err:
            print(err)
    return x

print('ax\N{SUPERSCRIPT TWO} + bx + c = 0')
a = get_float('enter a --> ', False)
b = get_float('enter b --> ', True)
c = get_float('enter c --> ', True)

x1 = None
x2 = None
disc = (b ** 2) - (4 * a * c)
if disc == 0:
    x1 = -(b / (2 * a))
else:
    if disc > 0:
        root = math.sqrt(disc)
    else:
        root = cmath.sqrt(disc)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    
equation = (f'{a}x\N{SUPERSCRIPT TWO}')
if b != 0:
    if b < 0:
        equation += f'- {abs(b)}'
    else:
        equation += f'+ {b}x'
if c != 0:
    if c < 0:
        equation += f'- {abs(c)}'
    else:
        equation += f'+ {c}'
equation += f'= 0 \N{RIGHTWARDS ARROW} x = {x1:.2f}'

if x2 is not None:
    equation += f' or x = {x2:.2f}'
print(equation)
            