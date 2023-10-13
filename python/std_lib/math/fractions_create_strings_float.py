#! /usr/bin/env python3 

import fractions

for s in ['0.5', '1.5', '2.0', '5e-1']:
    f = fractions.Fraction(s)
    
    print(f'{s:>4} = {f}')