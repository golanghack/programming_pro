#! /usr/bin/env python3 

import heapq
import random

random.seed(2016)

data = []

for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)
    
for i, d in enumerate(data):
    print(f'{i} -> {d}')
    
print('\nMerged -> ')
for i in heapq.merge(*data):
    print(i, end=' ')
print()