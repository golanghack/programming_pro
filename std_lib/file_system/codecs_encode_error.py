#! /usr/bin/env python3 

import codecs 
import sys 

error_handling = sys.argv[1]

text = 'Français'

try:
    # safe data in ASCII use errors handler in cli
    with codecs.open('encode_error.txt', 'w', encoding='ascii', errors=error_handling) as file_:
        file_.write(text)
        
except UnicodeDecodeError as err:
    print('!!!ERROR!!!', err)
    
else:
    # if no errors 
    with open('encode_error.txt', 'rb') as file_:
        print(f'File contents -> {file_.read()!r}')