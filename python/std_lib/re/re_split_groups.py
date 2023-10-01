#!  /usr/bin/env python3 

import re 

text: str = """ 
Paragraph one 
on two lines.

Paragraph two.


Paragraph three.
"""

print('With split -> ')
for num, paragraph in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(paragraph))
    print()