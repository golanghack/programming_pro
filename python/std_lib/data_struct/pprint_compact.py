#! /usr/bin/env python3 

from pprint import pprint
from pprint_data import data

print('DEFAULt -> ')
pprint(data, compact=False)
print('COMPACT -> ')
pprint(data, compact=True)