#! /usr/bin/env python3 

import asyncio
import logging 
from asyncio import StreamReader, StreamWriter


class ChatServer:
    
    def __init__(self):
        self._username_to_writer = {}
        
    async def start_chat_server(self, host: str, port: int):
        server = await asyncio.start_server(self.client_connected, host, port)
        
        async with server:
            await server.serve_forever()
            
    async def client_connected(self, reader: StreamReader, writer: StreamWriter):
        # wait while client send name
        # or agains unconnect
        command = await reader.readline()
        
        print(f'Connected -> {reader}{writer}')
        command, args = command.split(b' ')
        if command == b'CONNECT':
            username = args.replace(b'\n', b'').decode()
            self._add_user(username, reader, writer)
            await self._on_connected(username, writer)
        else:
            logging.error('Got uncorrect command from client, switch off')
            writer.close()
            await writer.wait_closed()
            
    def _add_user(self, username: str, reader: StreamReader, writer: StreamWriter):
        self._username_to_writer[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))
        
    async def _on_connected(self, username: str, writer: StreamWriter):
        # after jconnected user push all users
        writer.write(f'Welcome. Connected users -> {len(self._username_to_writer)}\n'.encode())
        await writer.drain()
        await self._notify_all(f'Connected {username}\n')
        
    async def _remove_user(self, username: str):
        writer = self._username_to_writer[username]
        del self._username_to_writer[username]
        
        try:
            writer.close()
            await writer.wait_closer()
        except Exception as err:
            logging.exception('Error for closed client writer,ignoring', exc_info=err)
            
    async def _listen_for_messages(self, username: str, reader: StreamReader):
        # listen messages from client and push all client
        # timer unless minute
        try:
            while (data := await asyncio.wait_for(reader.readline(), 60)) != b'':
                await self._notify_all(f'{username} -> {data.decode()}')
                await self._notify_all(f'{username} has left the chat\n')
        except Exception as err:
            logging.exception('Error for readeing data from client', exc_info=err)
            await self._remove_user(username)
            
    async def _notify_all(self, message: str):
        # send message all client connected and remove clients
        inactive_users = []
        for username, writer in self._username_to_writer.items():
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as err:
                logging.exception('Error with recors data for client', exc_info=err)
                inactive_users.append(username)
        [await self._remove_user(username) for username in inactive_users]
        
async def main():
    chat_server = ChatServer()
    await chat_server.start_chat_server('127.0.0.1', 8000)        
    
    
asyncio.run(main())