#! /usr/bin/env python3 

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.6}]
print(f'DATA -> {repr(data)}')

data_string = json.dumps(data)
print(f'JSON -> {data_string}')