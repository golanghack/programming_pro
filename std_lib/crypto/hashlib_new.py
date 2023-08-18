#! /usr/bin/env python3 

import argparse
import hashlib
import sys
from hashlib_data import lorem

parser = argparse.ArgumentParser('hashlib demo')
parser.add_argument('hash_name', 
                    choices=hashlib.algorithms_available, 
                    help='the name of the hash algo to use',)
parser.add_argument(
    'data', 
    nargs='?',
    default=lorem, 
    help='the input data to hash, defaults to lorem',)
args = parser.parse_args()

hashing = hashlib.new(args.hash_name)
hashing.update(args.data.encode('utf-8'))
print(hashing.hexdigest())