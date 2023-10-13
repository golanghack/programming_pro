#! /usr/bin/env python3 

import re 

text: str = 'aabbbbbaaaabbbaaabbbaaaaa'
pattern: str = 'ab'

for match in re.finditer(pattern, text):
    start = match.start()
    end = match.end()
    print(f'Found -> {text[start:end]!r} at -> {start:d}:{end:d}')