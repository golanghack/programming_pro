#! /usr/bin/env python3 

import re 

text: str = 'This is some text -- with punctuation.'
pattern: str = 'is'

print('<<<--Text -> ', text)
print('<<<--Pattern -> ', pattern)

result = re.search(pattern, text)
print('<<<--Search -> ', result)

fullmatch = re.fullmatch(pattern, text)
print('<<<--Full match -> ', fullmatch)
