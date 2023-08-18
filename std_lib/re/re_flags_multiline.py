#! /usr/bin/env python3 

import re 

text: str = 'This is some text --with punctuation.\nA second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print(f'Text -> \n {text!r}')
print(f'Pattern -> \n {pattern}')
print('Single line -> ')
for match in single_line.findall(text):
    print(f'  {match!r}')
print('Multiline -> ')
for match in multiline.findall(text):
    print(f'  {match!r}')