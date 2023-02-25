#! /usr/bin/env python3 

import codecs
import io 
from codecs_to_hex import to_hex

# row data 
data = 'Français'

# encoding with UTF-8
utf8 = data.encode('utf-8')
print('Start as UTF-8 -> ', to_hex(utf8, 1))

# set out buffer and wrapping class EncodeFile
output = io.BytesIO()
encoded_file = codecs.EncodedFile(output, data_encoding='utf-8', file_encoding='utf-16')
encoded_file.write(utf8)

# from buffer as a bytes string in utf-16
utf16 = output.getvalue()
print('Encoded to UTF-16 -> ', to_hex(utf16, 2))

# another by=uffer for reading data utf-16
# and wrapping another class EncodedFile
buffer = io.BytesIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8', file_encoding='utf-16')

# read data in utf-8
recoded = encoded_file.read()
print('Back to UTF-8 -> ', to_hex(recoded, 1))