#! /usr/bin/env python3 

import re 

text: str = """ 
Paragraph one 
on two lines.
Paragraph two.
Paragraph three.
"""

for line_number, paragraph in enumerate(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)):
    print(line_number, repr(paragraph))
    print()
    