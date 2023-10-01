#! /usr/bin/env python3 

import zlib 
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'rb') as input_:
    while True:
        block = input_.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print(f'Compressed -> {binascii.hexlify(compressed)}')
            
        else:
            print('buffering -> ')
    remaining = compressor.flush()
    print(f'Flushed  -> {binascii.hexlify(remaining)}')