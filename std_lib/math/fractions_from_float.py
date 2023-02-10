#! /usr/bin/env python3 

import fractions 

for v in [0.1, 0.2, 0.5, 2.0]:
    f = fractions.Fraction(v)
    print(f'{v} = {f}')