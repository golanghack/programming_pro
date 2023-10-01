#! /usr/bin/env python3

import math 

for i in range(6):
    print(f'{i} / 2 -> {math.modf(i / 2.0)}')