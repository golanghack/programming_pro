#! /usr/bin/env python3 

import codecs
import sys 
from codecs_to_hex import to_hex

error_handling = sys.argv[1]

text = 'Français'
print('Original -> ', repr(text))

# safe data with any coding
with codecs.open('decode_error.txt', 'w', encoding='utf-16') as file_:
    file_.write(text)
    
# output bytes 
with open('decode_error.txt', 'rb') as file_:
    print('File contens -> ', to_hex(file_.read(), 1))
    
# try read data with uncorrect encode
with codecs.open('decode_error.txt', 'r', encoding='utf-8', errors=error_handling) as file_:
    try:
        data = file_.read()
    except UnicodeDecodeError as err:
        print('!!!ERROR!!!', err)
    else:
        print('Read -> ', repr(data))