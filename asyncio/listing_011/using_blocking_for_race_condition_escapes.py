#! /usr/bin/env python3 

import asyncio 
from asyncio import Lock

class MockSocket:
    
    def __init__(self):
        self.socket_closed = False
        
    async def send(self, msg: str):
        if self.socket_closed:
            raise Exception('Socket close')
        print(f'Sending {msg}')
        await asyncio.sleep(1)
        print(f'Sent {msg}')
        
    def close(self):
        self.socket_closed = True
        
user_names_to_socket = {
    'Anna': MockSocket(), 
    'Bill': MockSocket(), 
    'Gram': MockSocket(), 
    'Eric': MockSocket(), 
}

async def user_disconnect(username: str, user_lock: Lock):
    print(f'{username} turn off')
    async with user_lock:
        print(f'{username} remove from dict of users')
        socket = user_names_to_socket.pop(username)
        socket.close()
        
async def message_all_users(user_lock: Lock):
    print('Create tasks sending messages')
    async with user_lock:
        messages = [socket.send(f'Hello {user}') for user, socket in user_names_to_socket.items()]
        await asyncio.gather(*messages)

async def main():
    user_lock = Lock()
    await asyncio.gather(message_all_users(user_lock), user_disconnect('Eric', user_lock))
    
asyncio.run(main())
    