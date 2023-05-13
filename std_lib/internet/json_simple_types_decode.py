#! /usr/bin/env python3 

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 4.5}]
print(f'DATA -> {data}')

data_string = json.dumps(data)
print(f'ENCODED -> {data_string}')

decoded = json.loads(data_string)
print(f'DECODED -> {decoded}')

print('ORIGINAL -> ', type(data[0]['b']))
print('DECODED -> ', type(decoded[0]['b']))
