#! /usr/bin/env python3 

import re 

text: str = 'This is some text -- with punctuation.'

print(f'<<<--{text}-->>>')
print()

patterns = [
    (r'^(\w+)', 'word at start of string'),
    (r'(\w+)\s*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+) \W+(\w+', 'word starting with t, another word'),
    (r'(\w+t)\b', 'word ending with t'),
]

for pattern, description in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print(f'"{pattern}" ({description})\n')
    print(' ', match.groups())
    print()