#! /usr/bin/env python3

import math 

for i in [0, 1.1, 2.3, 4.4, 5.5, 6.6]:
    try:
        print(f'{i:2.1f} -> {math.gamma(i):6.2f}')
    except ValueError as err:
        print(f'ERROR -> computing gamma -> ({i}) -> err -> {err}')