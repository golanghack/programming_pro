#! /usr/bin/env python3 

from multiprocessing.managers import SyncManager, ListProxy



class Connection(SyncManager):
    
    def __init__(self, address: str):
        self.register('get_messages', 
                      proxytype=ListProxy)
        super().__init__(address=address, 
                         authkey=b'mysecretchat')
        self.connect()
        
    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)
class ChatClient:
    
    def __init__(self, nickname: str, 
                 connection_provider=Connection):
        self.nickname = nickname
        self._connection = None
        self._connection_provider = connection_provider
        self._last_msg_idx = 0 
        
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._connection_provider(('localhost', 9090))
        return self._connection
        
    def send_message(self, message: str):
        sent_message = f'{self.nickname}: {message}'
        self.connection.broadcast(sent_message)
        return sent_message
    
    def fetch_messages(self):
        messages = list(self.connection.get_messages())
        new_messages = messages[self._last_msg_idx:]
        self._last_msg_idx = len(messages)
        return new_messages
    
    
