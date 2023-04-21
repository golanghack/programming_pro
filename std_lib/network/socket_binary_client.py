#! /usr/bin/env python3 

import binascii
import socket
import struct
import sys 

# create TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 3.14)
packer = struct.Struct('I as f')
packed_data = packer.pack(*values)

print('values = ', values)

try:
    # send 
    print(f'sending -> {binascii.hexlify(packed_data)}')
    sock.sendall(packed_data)
finally:
    print('closing socket')
    sock.close()