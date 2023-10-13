#! /usr/bin/env python3 

import socket
import sys 

# create UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message'

try:
    # send data
    print(f'sending {message!r}')
    sent = sock.sendto(message, server_address)

    # get data
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print(f'received {data!r}')

finally:
    print('closing socket')
    sock.close()