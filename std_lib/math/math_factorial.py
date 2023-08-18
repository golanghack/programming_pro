#! /usr/bin/env python3 

import math 

for i in [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.1]:
    try:
        print(f'{i:2.0f} {math.factorial(i):6.0f}')
    except ValueError as err:
        print(f'Error computing factorial -> ({i}) -> err -> {err}')