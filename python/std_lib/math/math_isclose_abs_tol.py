#! /usr/bin/env python3 

import math 

INPUTS = [
    (1.0, 1.0 + 1e-07, 1e-08), 
    (1.0, 1.0 + 1e-08, 1e-08), 
    (1.0, 1.0 + 1e-09, 1e-08),
]

for a, b, abs_tol in INPUTS:
    close = math.isclose(a, b, abs_tol=abs_tol)
    abs_diff = abs(a - b)
    print(f'{a:8.2f} {b:11} {abs_tol:8} {abs_diff:0.9f} {close!s:>8}')