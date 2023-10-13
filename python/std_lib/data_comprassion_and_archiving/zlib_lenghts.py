#! /usr/bin/env python3 

import zlib 

original = b'This is the original text'

template = '{:>15} {:>15}'

print(template.format('len(data)', 'len(compressed)'))
print(template.format('-' * 15, '-' * 15))

for i in range(5):
    data = original * i 
    compressed = zlib.compress(data)
    highlight = '*' if len(data) < len(compressed) else ''
    print(template.format(len(data), len(compressed), highlight))