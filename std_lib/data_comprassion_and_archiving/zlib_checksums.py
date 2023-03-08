#! /usr/bin/env python3 

import zlib 

data = open('lorem.txt', 'rb').read()

cksum = zlib.adler32(data)

print(f'Adler32 -> {cksum:12d}')
print(f'        -> {zlib.adler32(data, cksum)}')

cksum = zlib.crc32(data)
print(f'CRC-32 -> {cksum}')
print(f'       -> {zlib.crc32(data, cksum):12d}')