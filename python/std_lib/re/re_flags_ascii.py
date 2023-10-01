#! /usr/bin/env python3 

import re

text: str = u'সুপ্ৰভাত'
text2: str = 'Καλημέρα'
pattern = r'\w+'
ascii_pattern = re.compile(pattern, re.ASCII)
unicode_pattern = re.compile(pattern)

print('Text -> ', text)
print('Pattern -> ', pattern)
print('ASCII -> ', list(ascii_pattern.findall(text)))
print('Unicode -> ', list(unicode_pattern.findall(text)))
print()
print()
print('Text -> ', text2)
print('Pattern -> ', pattern)
print('ASCII -> ', list(ascii_pattern.findall(text2)))
print('Unicode -> ', list(unicode_pattern.findall(text2)))