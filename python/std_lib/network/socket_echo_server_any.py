#! /usr/bin/env python3 

import socket 
import sys 

# create TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# glue socket for port on server
server_address = ('', 10000)
sock.bind(server_address)
print('starting up on {} port {}'.format(*sock.getsockname()))
sock.listen(1)

while True:
    print('waiting connection')
    connection, client_address = sock.accept()
    try:
        print('connection with client -> ', client_address)
        while True:
            data = connection.recv(64)
            print(f'received -> {data!r}')
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()