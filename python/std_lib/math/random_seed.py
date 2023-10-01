#! /usr/bin/env python3 

import random

random.seed(1)

for i in range(5):
    print(f'{random.random():04.3f}', end=' ')
print()