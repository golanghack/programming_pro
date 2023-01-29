#! /usr/bin/env python3 


import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random data -> ', data)
print()

for n in data:
    print(f'add -> {n:>3} ->')
    heapq.heappush(heap, n)
    show_tree(heap)