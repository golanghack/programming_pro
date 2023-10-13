#! /usr/bin/env python3 

import heapq
from heapq_heapdata import data

print('all ->', data)
print('3 largest -> ', heapq.nlargest(3, data))
print('from sort -> ', list(reversed(sorted(data)[-3:])))
print('3 smaller -> ', heapq.nsmallest(3, data))
print('from sort -> ', sorted(data)[:3])