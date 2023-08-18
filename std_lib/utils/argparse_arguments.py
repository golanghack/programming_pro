#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='<--Example nonoptional-->')
parser.add_argument('count', action='store', type=int)
parser.add_argument('units', action='store')

print(parser.parse_args())