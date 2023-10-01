#! /usr/bin/env python3 

import re

text: str = 'This is some text -- with punctuation.'

print('Inputted text -> ', text)

#word staring from 't' followed another word
regex = re.compile(r'(\bt\w+) \W+(\w+)')
print('Pattern -> ', regex.pattern)

match = regex.match(text)
try:
    print('Entire match -> ', match.group(0))
    print('Word starting with "t" -> ', match.group(1))
    print('Word after "t" word -> ', match.group(2))
except AttributeError as err:
    print('Entire match -> ', match)
    print('Word starting with "t" -> ', match)
    print('Word after "t" word -> ', match)