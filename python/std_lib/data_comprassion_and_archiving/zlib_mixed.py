#! /usr/bin/env python3 

import zlib 

lorem = open('lorem.txt', 'rb').read()

compressed = zlib.compress(lorem)
combine = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combine)

decompressed_matches = decompressed == lorem

print('Decompressed matches lorem -> ', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem -> ', unused_matches)