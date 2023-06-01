#! /usr/bin/env python3 


""" 
PROBLEM 
want to make a list of the largest or smallest N items in a collection.
""" 

import heapq


portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda small: small['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda large: large['price'])

print(f'small -> {cheap}')
print(f'large -> {expensive}')