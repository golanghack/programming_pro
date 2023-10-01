#! /usr/bin/env python3 

import codecs
from codecs_to_hex import to_hex

# read row data 
with open('nonnative-ecnoded.txt', mode='rb') as file_:
    raw_bytes = file_.read()
    
print('Row -> ', to_hex(raw_bytes, 2))

# again open file and find BOM with codecs module
with codecs.open('nonative-encoded.txt', mode='r', encoding='utf-16') as file_:
    decoded_text = file_.read()
    
print('Decoded -> ', repr(decoded_text))
