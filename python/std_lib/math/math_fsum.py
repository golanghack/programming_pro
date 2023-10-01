#! /usr/bin/env python3 

import math 

values = [0.1] * 10 

print('Input values -> ', values)
print(f'sum() -> {sum(values):.20f}')

s = 0.0 
for i in values:
    s += i 
    
print(f'for-loop -> {s:.20f}')

print(f'math.fsum() -> {math.fsum(values):.20f}')