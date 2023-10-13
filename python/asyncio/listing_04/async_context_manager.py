#! /usr/bin/env python3 

import asyncio 
import socket
from types import TracebackType
from typing import Optional, Type 

class ConnectedSocket:
    """Connection."""
    
    def __init__(self, server_socket: socket.socket()) -> None:
        self._connection = None
        self._server_socket = server_socket
    
    # enter in with block 
    # waiting connection with client    
    async def __aenter__(self):
        print('Enter in context manager, waiting connection')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print('Confirm connection')
        return self._connection
    
    # call for exit from block with 
    # close connection
    async def __aexit__(self, 
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        print('Exit from context manager')
        self._connection.close()
        print('Close connection')
        
async def main() -> None:
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8002)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    
    # call __aenter__ -> waiting connection
    async with ConnectedSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)
        # __aexit__
        
asyncio.run(main())
        