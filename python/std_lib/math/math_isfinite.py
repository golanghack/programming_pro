#! /usr/bin/env python3 

import math 

for f in [0.0, 1.0, math.pi, math.e, math.inf, math.nan]:
    print(f'{f:5.2f} {math.isfinite(f)!s}')