#! /usr/bin/env python3 

import binascii
import ipaddress

ADDRESSES = [
    '10.0.0.6', 
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print(f'{addr!r}')
    print('     IP version -> ', addr.version)
    print('     is private -> ', addr.is_private)
    print('   packet form  -> ', binascii.hexlify(addr.packed))
    print('        integer -> ', int(addr))
    print()