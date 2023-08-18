#! /usr/bin/env python3 

import fractions

for s in ['1/2', '2/4', '3/6']:
    f = fractions.Fraction(s)
    print(f'{s} = {f}')