#! /usr/bin/env python3 

import socket
import sys

def get_constants(prefix: str) -> dict:
    """Create dict for constants and module socket names."""

    return {
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# create socxket TCP/IP
sock = socket.create_connection(('localhost', 10000))

print('family -> ', families[sock.family])
print('Type -> ', types[sock.type])
print('Protocol -> ', protocols[sock.proto])
print()

try:
    # send data 
    message = b'This is the message'
    print(f'sending {message!r}')
    sock.sendall(message)

    amount_received = 0 
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f'received {data!r}')
finally:
    print('closing socket connection')
    sock.close()