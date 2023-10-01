#! /usr/bin/env python3 

import re 

text: str = 'this is some text -- with punctuation.\nA second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print(f'Text -> \n {text!r}')
print(f'Pattern ->\n {pattern}')
print('No newlines -> ')
for match in no_newlines.findall(text):
    print(f'  {match!r}')
print('Dotall    -> ')
for match in dotall.findall(text):
    print(f'  {match!r}')
    