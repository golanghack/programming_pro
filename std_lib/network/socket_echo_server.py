#! /usr/bin/env python3 

import socket
import sys 

# create socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# listen connection 
sock.listen(1)

while True:
    # wait connection
    print('waiting for a connection')
    connection, client_addr = sock.accept()
    try:
        print('connection from', client_addr)

        # less parts date and send back
        while True:
            data = connection.recv(64)
            print(f'received {data!r}')
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_addr)
                break
    finally:
        connection.close()