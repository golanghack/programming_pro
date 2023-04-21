#! /usr/bin/env python3 

import socket
import sys 

# create socket UDS 
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# connect to port 
server_address = './uds_socket'
print(f'connection to {server_address}')

try:
    sock.connect(server_address)
except socket.error as message:
    print(message)
    sys.exit(1)

try:
    # send data 
    message = b'This is the message'
    print(f'sending -> {message!r}')
    sock.sendall(message)

    amount_received = 0 
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f'received {data!r}')


finally:
    print('closing')
    sock.close()