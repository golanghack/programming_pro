#! /usr/bin/env python3 

import asyncio
import socket
from asyncio import AbstractEventLoop

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """This function working one connection."""
    
    while data := await loop.sock_recv(connection, 1024): # wait data from client
        await loop.sock_sendall(connection, data) # sent data -> return back client
        
async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    """Listener for connection."""
    
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Got connection from {address}')
        asyncio.create_task(echo(connection, loop))
        
async def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = ('127.0.0.1', 8001)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    
    await listen_for_connection(server_socket, asyncio.get_event_loop())
    
asyncio.run(main())
        
    
