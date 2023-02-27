#! /usr/bin/env python3 

import pickle
from pprint import pprint

data_1 = [
    {
        'a': 'A',
        'b': 2, 
        'c': 3.0,
    },
]

print('BEFORE -> ', end=' ')
pprint(data_1)

data1_string = pickle.dumps(data_1)

data_2 = pickle.loads(data1_string)
print('AFTER -> ', end=' ')
pprint(data_2)

print('SAME? -> ', (data_1 is data_2))
print('EQUAL? -> ', (data_1 == data_2))

