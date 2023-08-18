#! /usr/bin/env python3 

import socket
import sys 

# create TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket glue to address in cmd
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected -> ', client_address)
        while True:
            data = connection.recv(64)
            print(f'received {data!r}')
            if data: 
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()