#! /usr/bin/env python3 

import asyncio
from asyncio import Transport, Future, AbstractEventLoop
from typing import Optional


class HTTPGetClientProtocol(asyncio.Protocol):
    
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host: str = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b''
        
    async def get_response(self):
        """ 
        Wait into Future object while dont response 
        from server.
        """
        
        return await self._future
    
    def _get_request_bytes(self) -> bytes:
        """Create PPE request."""
        
        request = f'GET / HTTP/1.1\r\n'\
                  f'Connection: close\r\n'\
                  f'Host: {self._host}\r\n\r\n'
        return request.encode()
    
    def connection_made(self, transport: Transport) -> None:
        print(f'Create connection to {self._host}')
        self._transport = transport
        # after connected use transport for request
        self._transport.write(self._get_request_bytes())
        
    def data_received(self, data: bytes) -> None:
        print(f'Taked data -> {data}')
        # safe data in into buffer
        self._response_buffer = self._response_buffer + data
        
    def eof_received(self) -> Optional[bool]:
        # after connection close finish Future object copy data from buffer
        self._future.set_result(self._response_buffer.decode())
        return False
    
    def connection_lost(self, exc: Optional[Exception]) -> None:
        """ 
        If connection lost without errors dont do.
        if connection lost with errors finish Future object with exception"""
        
        if exc is None:
            print('Connection close without errors.')
        else:
            self._future.set_exception(exc)
            
            
        