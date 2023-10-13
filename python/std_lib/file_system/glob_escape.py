#! /usr/bin/env python3 

import glob 

specials = '?*['

for char in specials:
    pattern = 'dir/*' + glob.escape(char) + '.txt'
    print(f'Searching for -> {pattern!r}')
    for name in sorted(glob.glob(pattern)):
        print(name)
    print()