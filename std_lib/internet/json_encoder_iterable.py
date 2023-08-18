#! /usr/bin/env python3 

import json

encoder = json.JSONEncoder()
data = [{'a': 'A', 'b': (9, 8), 'c': 8.0}]

for part in encoder.iterencode(data):
    print('PART -> ', part)