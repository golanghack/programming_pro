#! /usr/bin/env python3 

import math 

print('{:^4} {:^4} {:^5} {:^5}'.format('x', 'y', '%', 'fmod'))
print('{:-^4} {:-^4} {:-^5} {:-^5}'.format('-', '-', '-', '-'))

INPUTS = [
    (11, 6), 
    (11, -6), 
    (-11, 6),
]

for x, y in INPUTS:
    print(f'{x:4.1f} {y:4.1f} {x % y:5.2f} {math.fmod(x, y):5.2f}')