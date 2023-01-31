#! /usr/bin/env python3 

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
print('Original values -> ', values)

ends = [
    ('@', 'native, native'),
    ('=', 'native, standart'),
    ('<', 'little-endian'),
    ('>', 'big-endian'), 
    ('|', 'network'),
]

for code, name in ends:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print()
    print()
    print('Format string -> ', s.format, 'for', name)
    print('Uses          -> ', s.size, 'bytes')
    print('Packed Value  -> ', binascii.hexlify(packed_data))
    print('Unpacked Value-> ', s.unpack(packed_data))