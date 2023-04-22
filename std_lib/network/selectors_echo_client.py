#! /usr/bin/env python3 

import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'It will be repeated', 
    b'This is the message',
]

bytes_sent = 0 
bytes_received = 0 

# connection -> blocking operation 
# after made connection call method setblocking()
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# setting selector for monitoring made on socket for send data
# and data for read
mysel.register(
    sock, 
    selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print(f'client({client_address})')

        if mask and selectors.EVENT_READ:
            print('ready to read')
            data = connection.recv(1024)
            if data:
                # socket client for read got data 
                print(f'received {data!r}')
                bytes_received += len(data)
            
            # take down for empty result
            keep_running = not (
                data or (bytes_received and (bytes_received == bytes_sent))
            )

        if mask and selectors.EVENT_READ:
            print('ready to read')
            data = connection.recv(1024)
            if data:
                # socket for read got data
                print(f'received {data!r}')
                bytes_received += len(data)

            # break 
            keep_running = not (
                data or 
                (bytes_received and (bytes_received == bytes_sent))
            )
        if mask and selectors.EVENT_WRITE:
            print('ready to write')
            if not outgoing:
                # message is not 
                # change register only read 
                print('switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # send next message 
                next_msg = outgoing.pop()
                print(f'sending {next_msg!r}')
                sock.sendall(next_msg)

print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()