#! /usr/bin/env python3 

import getpass
import sys 

if sys.stdin.isatty():
    password = getpass.getpass('Using gp -> ')
else:
    print('Using readline -> ')
    password = sys.stdin.readline().rstrip()
print(f'Read -> {password}')