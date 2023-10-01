#! /usr/bin/env python3 

import socket
import sys 

# create UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# glue socket for port
server_address = ('localhost', 10000)
print('starting up on {} port{}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print(f'received {len(data)} bytes from {address}')
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print(f'sent {sent} bytes back to {address}')