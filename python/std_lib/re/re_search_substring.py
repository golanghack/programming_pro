#! /usr/bin/env python3 

import re 

text: str = 'This is some text -- with punctuatiion.'
pattern = re.compile(r'\b\w*is\w*\b')

print('<<< Text -> ', text)
print()

position = 0
while True:
    _match = pattern.search(text, position)
    if not _match:
        break
    start = _match.start()
    end = _match.end()
    print(f'<<<{start:>2d} <<>> {end-1:>2d} = "{text[start:end]}"')
    #move front on string text for searching 
    position = end
    