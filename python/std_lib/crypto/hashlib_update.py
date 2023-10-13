#! /usr/bin/env python3 

import hashlib
from hashlib_data import lorem 

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()

def chunkize(size, text):
    """Return parts of the text in size-based increments."""
    
    start = 0 
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return 


h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)

line_by_line = h.hexdigest()

print('all at once -> ', all_at_once)
print('line by line -> ', line_by_line)
print('same           -> ', (all_at_once == line_by_line))