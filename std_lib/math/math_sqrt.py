#! /usr/bin/env python3 

import math

print(math.sqrt(9.0))
print(math.sqrt(3))

try:
    print(math.sqrt(-1))
except ValueError as err:
    print(f'Cannot compute sqrt(-1) -> {err}')