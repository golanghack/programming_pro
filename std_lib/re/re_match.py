#! /usr/bin/env python3

import re 

text: str = 'This is some text -- with punctuation.'
pattern: str = 'is'

print('<<<--Text -> ', text)
print('<<<--Pattern -> ', pattern)

_match = re.match(pattern, text)
print('<<<--Match -> ', _match)

_search = re.search(pattern, text)
print('<<<--Search -> ', _search)