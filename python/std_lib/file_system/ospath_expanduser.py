#! /usr/bin/env python3 

import os.path

for user in ['', 'one', 'two']:
    lookup = '~' + user
    print(f'{lookup!r:>15} -> {os.path.expanduser(lookup)}')