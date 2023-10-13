#! /usr/bin/env python3 

import json

data = [{'a': 'A', 'b': (3, 5), 'c': 8.0}]
print(f'DATA -> {repr(data)}')
print('repr(data) -> ', len(repr(data)))

plain_dump = json.dumps(data)
print('dumps(data) -> ', len(plain_dump))

small_indent = json.dumps(data, indent=2)
print('dumps(data, indent=2) -> ', len(small_indent))

with_separators = json.dumps(data, separators=(',', ':'))
print('dumps(data, separators) -> ', len(with_separators))