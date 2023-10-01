#! /usr/bin/env python3 

import unicodedata
from codecs_to_hex import to_hex

text = 'Français'

print(f'Row -> {text!r}')
for c in text:
    print(f' {c!r} -> {unicodedata.name(c, c)}')

print(f'UTF-8 -> {to_hex(text.encode("utf-8"), 1)!r}')
print(f'UTF-16 -> {to_hex(text.encode("utf-16"), 2)!r}')