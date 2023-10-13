#! /usr/bin/env python3 

import codecs
import sys 

text = b'abcdef\n'
repetitions = 50

print('Text lenght -> ', len(text))
print('Repetitions -> ', repetitions)
print('Expected len -> ', len(text) * repetitions)

# do it many encoding text for create big data
encoder = codecs.getincrementalencoder('bz2')()
encoded = []

print()
print('Encoding -> ', end=' ')
last = repetitions - 1
for i in range(repetitions):
    en_c = encoder.encode(text, final=(i == last))
    if en_c:
        print(f'\nEncoded -> {len(en_c)} bytes')
        encoded.append(en_c)
    else:
        sys.stdout.write('.')
all_encoded = b''.join(encoded)
print()
print('Total encoded lendght -> ', len(all_encoded))
print()

# decode bytes string on one byte 
decoder = codecs.getincrementaldecoder('bz2')()
decoded = []

print('Decoding -> ', end=' ')
for i, b in enumerate(all_encoded):
    final= (i + 1) == len(text)
    c = decoder.decode(bytes([b]), final)
    if c:
        print(f'\nDecoded -> {len(c)} characters.')
        print('Decoding -> ', end=' ')
        decoded.append(c)
    else:
        sys.stdout.write('.')
print()

restored = b''.join(decoded)
print()
print('Total uncompressed lenght -> ', len(restored))