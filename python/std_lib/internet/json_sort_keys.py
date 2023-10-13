#! /usr/bin/env python3 

import json

data = [{'a': 12, 'b': (3, 4), 'c': 56.9}]
print(f'DATA -> {repr(data)}')

unsorted = json.dumps(data)
print(f'JSON -> {json.dumps(data)}')
print(f'SORT -> {json.dumps(data, sort_keys=True)}')

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('UNSORTED MATCH -> ', unsorted == first)
print('SORTED MATCH -> ', first == second)