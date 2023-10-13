#! /usr/bin/env python3 

from multiprocessing.managers import SyncManager

class Connection(SyncManager):
    
    def __init__(self, address: str) -> None:
        self.register('get_messages')
        super().__init__(address=address, authkey=b'mychatsecret')
        self.connect()
        
    def broadcast(self, message: str):
        messages = self.get_messages()
        messages.append(message)
        
messages = []
"""
def _srv_get_messages():
    return _messages 

class _ChatServerManager(SyncManager):
    pass

_ChatServerManager.register('get_messages', callable=_srv_get_messages,
                            proxytype=ListProxy)

def new_chat_server():
    return _ChatServerManager(('', 9090), authkey=b'mychatsecret')
"""