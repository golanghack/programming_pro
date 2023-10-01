#! /usr/bin/env python3 

import socket
import struct
import sys 

multicast_group = '224.3.29.71'

server_address = ('', 10000)

# create socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# glue socket to port
sock.bind(server_address)

# speak OS add socket in multicast group all interfaces
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# loop request/response
while True:
    print('\nwaituing to receive message')
    data, address = sock.recvfrom(1024)

    print(f'received {len(data)} bytes from {address}')
    print(data)

    print('sending acknounedgement to ', address)
    sock.sendto(b'ack', address)