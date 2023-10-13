#! /usr/bin/env python3 

""" 
PROBLEM 
want to make a list of the largest or smallest N items in a collection.
""" 

import heapq

nums = [99, 88, 55, 3, 4, 5, 77, 88, 99]

large = heapq.nlargest(3, nums)
small = heapq.nsmallest(3, nums)

print(f'first large 3 elems-> {large}')
print(f'first small 3 elems-> {small}')