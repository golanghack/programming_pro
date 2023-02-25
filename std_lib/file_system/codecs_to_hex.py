#! /usr/bin/env python3 

import binascii

def to_hex(t: str, nbytes: bytes) -> bytes:
    """ 
    Format text t as a bytes lenght nbytes separated indent.
    """
    
    chars_per_item = nbytes * 2 
    hex_version = binascii.hexlify(t)
    return b' '.join(hex_version[start:start + chars_per_item] 
                     for start in range(0, len(hex_version), chars_per_item))
if __name__ == '__main__':
    print(to_hex(b'abcdef', 1))
    print(to_hex(b'abcdef', 2))
    
    