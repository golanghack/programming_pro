#! /usr/bin/env python3 

import asyncio

class MockSocket:
    
    def __init__(self):
        self.socket_closed = False
        
    # imitation slow sending messages to cloent
    async def send(self, msg: str):
        if self.socket_closed:
            raise Exception('Socket close')
        print(f'Sending {msg}')
        await asyncio.sleep(1)
        print(f'Sent {msg}')
        
    def close(self):
        self.socket_closed = True
        
user_names_to_sockets = {
        'Anna': MockSocket(), 
        'Ben': MockSocket(), 
        'Gram': MockSocket(),
        'Di': MockSocket(),
    }

# turn off user and remove from memory
async def user_disconnect(username: str):
    print(f'{username} turn off')
    socket = user_names_to_sockets.pop(username)
    socket.close()
    
# sending message to all users concurency
async def message_all_users():
    print('Create tasks for messages sending')
    messages = [socket.send(f'Hello, {user}') for user, socket in user_names_to_sockets.items()]
    await asyncio.gather(*messages)
    
async def main():
    await asyncio.gather(message_all_users(), user_disconnect('Anna'))
    
asyncio.run(main())