#! /usr/bin/env python3 

import re

#pre-compilation patterns 
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text: str = 'Does this text match the pattern?'
print(f'Text -> {text!r}\n')

for regex in regexes:
    print(f'Seekeing -> "{regex.pattern}" -> ', end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match!')