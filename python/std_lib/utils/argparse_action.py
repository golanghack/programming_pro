#! /usr/bin/env python3 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store', 
                    dest='a_simple_value', 
                    help='A simple value')
parser.add_argument('-b', 
                    action='store_const', 
                    dest='const_value', 
                    const='value-to-store',
                    help='Store a constant value')
parser.add_argument('-c', 
                    action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-d', 
                    action='store_false',
                    default=True, 
                    dest='boolean_f',
                    help='Set a switch to false')
parser.add_argument('-e', 
                    action='append',
                    dest='collection',
                    default=[],
                    help='Add repeated values to a list')
parser.add_argument('-E', 
                    action='append_const',
                    dest='cont_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add diff values to list')
parser.add_argument('-D',
                    action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')
parser.add_argument('--version', 
                    action='version',
                    version='%(prog)s 1.0')

results = parser.parse_args()
print(f'simple_value          -> {results.a_simple_value!r}')
print(f'constant_value        -> {results.const_value!r}')
print(f'boolean_t             -> {results.boolean_t!r}')
print(f'boolena_f             -> {results.boolean_f!r}')
print(f'collection            -> {results.collection}')
print(f'const_collection      -> {results.cont_collection}')
