#! /usr/bin/env python3 

import functools
import selectors
import socket
from CustomFuture import CustomFuture
from selectors import BaseSelector

# set cocket read/write for future after get request
def accept_connection(future: CustomFuture, connection: socket):
    print(f'Got request for connection from {connection}')
    future.set_result(connection)

# register in selector function accept_connecttion and wait connection request
async def sock_accept(sel: BaseSelector, sock) -> socket:
    print('Rgister socket for connection listener')
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print('Listen requests for connection')
    connection: socket = await future
    return connection

async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('127.0.0.1', 8088),)
    sock.listen()
    sock.setblocking(False)

    print('Wait connection for socket')
    connection = await sock_accept(sel, sock)
    print(f'Got connection {connection}')


selector = selectors.DefaultSelector()
coro = main(selector)

# call send main coroutine
while True:
    try:
        state = coro.send(None)

        events = selector.select()

        for key, mask in events:
            print('Working events from selector')
            callback = key.data 
            callback(key.fileobj)
    except StopIteration as si:
        print('App finished')
        break
