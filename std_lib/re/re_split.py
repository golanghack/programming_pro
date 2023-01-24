#! /usr/bin/env python3 

import re 

text: str = """ 
Paragraph one 
on two lines.
Paragraph two.
Paragraph three.
"""

print('With findall -> ')
for num, paragraph in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print(num, repr(paragraph))
    print()
print()
print('With split -> ')
for num, paragraph in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(paragraph))
print()