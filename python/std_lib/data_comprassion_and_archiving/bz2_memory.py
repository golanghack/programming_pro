#! /usr/bin/env python3 

import bz2
import binascii

original = b'This is the original text.'
print(f'Original -> {len(original)} bytes')
print(original)

print()
compressed = bz2.compress(original)
print(f'Compressed -> {len(compressed)} bytes')

hex_version = binascii.hexlify(compressed)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i * 40: (i + 1) * 40])
    
print()
decompressed = bz2.decompress(compressed)
print(f'Decompressed -> {len(decompressed)} bytes')
print(decompressed)