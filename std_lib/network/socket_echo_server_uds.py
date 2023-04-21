#! /usr/bin/env python3 

import socket
import sys 
import os 

server_address = '/.uds_socket'

# socket is?
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address)
    raise

# create UDS 
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# glue socket to address
print(f'starting up on {server_address}')
sock.bind(server_address)

# listen connections 
sock.listen(1)

while True:
    # waiting connection
    print('waitung connection')
    connection, client_address = sock.accept()
    try:
        print('connection', client_address)
        # less parts of data and send back
        while True:
            data = connection.recv(64)
            print(f'received {data!r}')
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()