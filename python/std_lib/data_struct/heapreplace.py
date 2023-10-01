#! /usr/bin/env python3 

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random -> ', data)
heapq.heapify(data)
print('Start ->')
show_tree(data)

for n in [0, 13]:
    small = heapq.heapreplace(data, n)
    print(f'replace {small:>12} with {n:>2}')
    show_tree(data)