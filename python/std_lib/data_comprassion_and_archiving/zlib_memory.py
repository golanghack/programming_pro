#! /usr/bin/env python3 

import zlib 
import binascii

origin = b'This is the original text'
print('Original  -> ', len(origin), origin)

compressed = zlib.compress(origin)
print('Compressed -> ', len(compressed), binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed -> ', len(decompressed), decompressed)