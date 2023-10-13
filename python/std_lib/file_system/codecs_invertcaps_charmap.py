#! /usr/bin/env python3 

import codecs
import string 

# mapping every symbol on self 
decoding_map = codecs.make_identity_dict(range(256))

# create couples list orders for letters in Upper case and lower case
pairs = list(zip([ord(c) for c in string.ascii_lowercase], 
                [ord(c) for c in string.ascii_uppercase]))

# change map for lower case to upper case conversary
decoding_map.update({
    upper: lower 
    for (lower, upper) in pairs
})

decoding_map.update({
    lower: upper 
    for (lower, upper) in pairs
})

# creating codecs tables
encoding_map = codecs.make_encoding_map(decoding_map)

if __name__ == '__main__':
    print(codecs.charmap_encode('abcdEFG', 'strict', encoding_map))
    print(codecs.charmap_decode(b'absdEFG', 'strict', decoding_map))
    print(encoding_map == decoding_map)