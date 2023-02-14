#! /usr/bin/env python3 

import math 

print(f'{"X":^7} {"Y":^7} {"HYPOT":^10}')
print(f'{"":-^7} {"":-^7} {"":-^7}')

POINTS = [
    # simple 
    (1, 1),
    (-1, -1),
    (math.sqrt(2), math.sqrt(2)),
    
    # treangulum with sides -> 3-4-5
    (3, 4), 
    
    # points of circle
    (math.sqrt(2) / 2, math.sqrt(2) / 2), # pi / 4 rad
    (0.5, math.sqrt(3) / 2), # pi / 3 rad
]

for x, y in POINTS:
    hyp = math.hypot(x, y)
    print(f'{x:7.2f} {y:7.2f} {hyp:7.2f}')