#! /usr/bin/env python3 

import argparse

parser = argparse.ArgumentParser(
    description='Change the option prefix characters',
    prefix_chars='-+/',
)

parser.add_argument('+a', action='store_true', default=None, help='Turn A on',)
parser.add_argument('//noarg', '++noarg', action='store_true', default=False)

print(parser.parse_args())