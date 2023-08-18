#! /usr/bin/env python3 

import json

data = [{'a': 'A', 'b': (9, 8), 'c': 8.0}]
print(f'DATA -> {repr(data)}')

print('NORMAL -> ', json.dumps(data, sort_keys=True))
print('INDENT -> ', json.dumps(data, sort_keys=True, indent=2))