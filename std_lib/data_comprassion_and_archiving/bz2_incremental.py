#! /usr/bin/env python3 

import bz2
import binascii
import io 

compressor = bz2.BZ2Compressor()

with open('lorem.txt', 'rb') as input_file:
    while True:
        block = input_file.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print(f'Compressed -> {binascii.hexlify(compressed)}')
        else:
            print('buffering -> ')
    remining = compressor.flush()
    print(f'Flushed -> {binascii.hexlify(remining)}')