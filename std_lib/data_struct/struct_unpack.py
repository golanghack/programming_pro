#! /usr/bin/env python3 

import struct
import binascii

packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')
s = struct.Struct('I is f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values -> ', unpacked_data)