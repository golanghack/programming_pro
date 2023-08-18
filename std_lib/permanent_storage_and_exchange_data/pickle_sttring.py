#! /usr/bin/env python3 

import pickle
from pprint import pprint

data = [
    {
        'a': 'A', 
        'b': 2, 
        'c': 3.0,
    },
]

print('DATA -> ', end=' ')
pprint(data)

data_string = pickle.dumps(data)
print(f'PICKLE -> {data_string!r}')