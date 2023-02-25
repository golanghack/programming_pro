#! /usr/bin/env python3 

import codecs
from codecs_to_hex import to_hex

# choice unself version UTF-16
if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'
    
print('Native order -> ', to_hex(codecs.BOM_UTF16, 2))
print('Selected order -> ', to_hex(bom, 2))

# encoding text
encoded_text = 'Français'.encode(encoding)
print(f'{encoding:14} -> {to_hex(encoded_text, 2)}')


with open('nonnative-encoded.txt', mode='wb') as file_:
    # write chiosed mark order of bytes.
    file_.write(bom)
    # write a bytes string of encoding
    file_.write(encoded_text)