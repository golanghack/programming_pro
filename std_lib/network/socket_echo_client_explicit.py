#! /usr/bin/env python3 

import socket
import sys 

# create TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection socket in port server
server_address = (sys.argv[1], 10000)

print('connection to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'This is the message'
    print(f'sending {message!r}')
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f'received -> {data!r}')
finally:
    sock.close()