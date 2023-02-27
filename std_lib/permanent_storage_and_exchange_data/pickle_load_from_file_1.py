#! /usr/bin/env python3 

import pickle
from pprint import pprint
import sys 

filename = sys.argv[1]

with open(filename, 'rb') as input_file:
    while True:
        try:
            out = pickle.load(input_file)
        except EOFError:
            break
        else:
            print(f'READ -> {out.name}  ({out.name_backwards})')