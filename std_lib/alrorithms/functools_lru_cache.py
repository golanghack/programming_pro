#! /usr/bin/env python3 

import functools

@functools.lru_cache()
def expensive(a, b):
    print(f'expensive({a}, {b})')
    return a * b

MAX = 2

print('First set of calls -> ')

for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecond set of calls -> ')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nClearing cache -> ')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThirsd set of calls -> ')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

