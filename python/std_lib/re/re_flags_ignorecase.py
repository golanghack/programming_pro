#! /usr/bin/env python3 

import re 

text: str = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print(f'Pattern ->\n {pattern}')
print('Case-sensitive -> ')
for match in with_case.findall(text):
    print(f'  {match!r}')
print('Case-insensitive -> ')
for match in without_case.findall(text):
    print(f'  {match!r}')