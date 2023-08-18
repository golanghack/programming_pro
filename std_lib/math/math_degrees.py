#! /usr/bin/env python3 

import math 

INPUTS = [
    (0, 0), 
    (math.pi / 6, 30),
    (math.pi / 4, 45), 
    (math.pi / 3, 60), 
    (math.pi / 2, 90), 
    (math.pi, 180), 
    (3 * math.pi / 2, 270), 
    (2 * math.pi, 360), 
]

print('{:^8} {:^8} {:^8}'.format('Radians', 'Degrees', 'Expected'))
print('{:-^8} {:-^8} {:-^8}'.format('', '', ''))

for rad, expected in INPUTS:
    print(f'{rad:8.2f} {math.degrees(rad):8.2f} {expected:8.2f}')