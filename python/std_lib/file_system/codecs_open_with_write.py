#! /usr/bin/env python3 

from codecs_to_hex import to_hex
import codecs
import sys 

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Writing to -> ', filename)
with codecs.open(filename, mode='w', encoding=encoding) as file_:
    file_.write('Français')
    
    # find group bytes for used with to_hex()
nbytes = {
        'utf-8': 1, 
        'utf-16': 2, 
        'utf-32': 4,
    }.get(encoding, 1)
    
# mapping row bytes keeping in file
print('File contents -> ')
with open(filename, mode='rb') as file_:
    print(to_hex(file_.read(), nbytes))