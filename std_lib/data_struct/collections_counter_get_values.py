#! /usr/bin/env python3 

import collections 

c = collections.Counter('abbccdd')

for letter in 'abcdn':
    print(f'{letter} -> {c[letter]}')