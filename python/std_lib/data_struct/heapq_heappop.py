#! /usr/bin/env python3 

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random -> ', data)
heapq.heapify(data)
print('heapifiesd ->')
show_tree(data)

print()
for i in range(2):
    small = heapq.heappop(data)
    print(f' pop {small:>3} -> ')
    show_tree(data)