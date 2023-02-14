#! /usr/bin/env python3 

import math 

print(f'{"X1":^8} {"Y1":^8} {"X2":^8} {"Y2":^8} {"DISTANCE":^8}')
print(f'{"":-^8} {"":-^8} {"":-^8} {"":-^8} {"":-^8}')

POINTS = [
    ((5, 5), (6, 6)), 
    ((-6, -6), (-5, -5)), 
    
    # treangulum with sides -> 3-4-5
    ((0, 0,), (3, 4)), 
    ((-1, -1), (2, 3)),
]

for (x1, y1), (x2, y2) in POINTS:
    x = x1 - x2
    y = y1 - y2 
    hyp = math.hypot(x, y) 
    
    print(f'{x1:8.2f} {y1:8.2f} {x2:8.2f} {y2:8.2f} {hyp:8.2f}')