#! /usr/bin/env python3 

import re 

text: str = 'abbaaaaaaaaabbbbaaabbbaaa'
pattern: str = 'ab'

for match in re.findall(pattern, text):
    print(f'Found -> {match!r}')
