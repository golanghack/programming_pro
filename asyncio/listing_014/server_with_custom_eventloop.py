#! /usr/bin/env python3 

import socket
from CustomTask import CustomTask
from EventLoop import EventLoop

async def read_from_client(conn, loop: EventLoop):
    print(f'Reading data from cleint {conn}')
    try:
        while data := await loop.sock_recv(conn):
            print(f'Got data {data} from client')
    finally:
        loop.sock_close(conn)

async def listen_for_cnnections(sock, loop: EventLoop):
    while True:
        print('Waiting')
        conn, addr = await loop.sock_accept(sock)
        CustomTask(read_from_client(conn, loop), loop)
        print(f'New connection -> {sock}')

async def main(loop: EventLoop):
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('127.0.0.1', 8088))
    server_socket.listen()
    server_socket.setblocking(False)

    await listen_for_cnnections(server_socket, loop)

event_loop = EventLoop()
event_loop.run(main(event_loop))