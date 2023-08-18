#! /usr/bin/env python3 

import math
from typing import List, Tuple

INPUTS: List[Tuple]  = [
    # defaault used
    (2, 3),
    (2.1, 3.1),
    
    # always 1
    (1.0, 5),
    (2.0, 0), 
    
    # not a number (NaN -> nan)
    (2, float('nan')),
    
    # roots 
    (9.0, 0.5), 
    (27.0, 1.0 / 3), 
]

for x, y in INPUTS:
    print(f'{x:5.1f} ** {y:5.3f} -> {math.pow(x, y):6.3f}')