#! /usr/bin/env python3 

import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True

def read(connection, mask):
    """Callback function for events of read."""

    global keep_running

    client_address = connection.getpeername()
    print(f'read({client_address})')
    data = connection.recv(1024)
    if data:
        # socket client for read 
        print(f'received {data!r}')
        connection.sendall(data)
    else:
        # interpratation empty result as a closing connection 
        print('closing')
        mysel.unregister(connection)
        connection.close()
        # Main loop stop
        keep_running = False

def accept(sock, mask):
    """Callback function for new connections."""

    new_connection, addr = sock.accept()
    print(f'accept({addr})')
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('waitong for I/O')
    for key, mask in mysel.select(timeout=1):
        callback = key.data 
        callback(key.fileobj, mask)

print('shutting down')
mysel.close()