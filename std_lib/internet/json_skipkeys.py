#! /usr/bin/env python3 

import json

data = [{'a': 'A', 'b':(9, 9), 'c': 3.9, ('d',): 'D tuple'},]

print('First attemp')
try:
    print(json.dumps(data))
except TypeError as err:
    print(f'ERROR -> {err}')

print()
print('Second attemp')
print(json.dumps(data, skipkeys=True))