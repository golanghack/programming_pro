#! /usr/bin/env python3 

import random

for i in range(5):
    print(f'{random.uniform(1, 100):04.3f}', end=' ')
print()