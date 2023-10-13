#! /usr/bin/env python3 

import math 

for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
    try:
        print(f'{i:2.1f} -> {math.lgamma(i):.20f} -> {math.log(math.gamma(i)):20f}')
    except ValueError as err:
        print(f'ERROR -> computing lgamma({i}) -> {err}')