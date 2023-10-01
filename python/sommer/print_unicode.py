#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--PRINT UNICODE>"""

import sys 
import unicodedata

def print_unicode_table(words):
    """Return table of unicode symbols."""
    
    print(f'decimal   hex   chr   {"name":^40}')
    print(f'-------   ---   ---   {"":-<40}')
    
    code = ord(' ')
    end = min(0xD800, sys.maxunicode)
    
    while code < end:
        c = chr(code)
        name = unicodedata.name(c, '*** unknown ***')
        ok = True
        for word in words:
            if word not in name.lower():
                ok = False
                break
        if ok:
            print(f'{code:7} {code:5X} {code:^3c} {name.title()}')
        code += 1
        
words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ('-h', '--help'):
        print(f'Usage --> {sys.argv[0]} [string1 [string2 [... stringN]]]')
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(words)