#! /usr/bin/env python3

from PriorityQueue import PriorityQueue

def heap_sort(L):
    H = PriorityQueue(L)
    L[:] = [item for item in H]

# test 
L = [2, 3, 0, 1, 5, 6,]
print(f'BEFORE -> {L}')
heap_sort(L)
print(f'AFTER -> {L}')