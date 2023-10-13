#! /usr/bin/env python3 

import socket 
import sys 

messages = [
    'This is message', 
    'It will be sent',
]

server_address = ('localhost', 10000)

# create socket TCP/IP
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# connection socxket for port 
print('connecting to {} port {}'.format(*server_address), file=sys.stderr)
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()

    # send message both sockets
    for s in socks:
        print(f'{s.getsockname()} -> sending {outgoing_data!r}', file=sys.stderr)
        s.send(outgoing_data)
    for s in socks:
        data = s.recv(1024)
        print(f'{s.getsockname()} -> received {data!r}', file=sys.stderr)
        if not data:
            print('closing socket', s.getsockname(), file=sys.stderr)
            s.close()
