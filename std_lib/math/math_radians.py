#! /usr/bin/env python3 

import math 

print('{:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Expected'))
print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

INPUTS = [
    (0, 0), 
    (30, math.pi / 6), 
    (45, math.pi / 4), 
    (60, math.pi / 3), 
    (90, math.pi / 2), 
    (180, math.pi), 
    (270, 3 / 2.0 * math.pi), 
    (360, 2 * math.pi), 
]

for degree, expected in INPUTS:
    print(f'{degree:7d} {math.radians(degree):7.2f} {expected:7.2f}')