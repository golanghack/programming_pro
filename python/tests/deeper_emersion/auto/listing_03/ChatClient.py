#! /usr/bin/env python3 

from typing import Any
from Connection import Connection

class ChatClient:
    
    def __init__(self, nickname: str, connection_provider=Connection):
        self.nickname = nickname
        self._connection = None
        self._connection_provider = connection_provider
        self._last_msg_idx = 0
        
    def send_message(self, message: Any) -> str:
        sent_message = f'{self.nickname}: {str(message)}'
        self.connection.broadcast(sent_message)
        return sent_message
    
    def fetch_messages(self):
        messages = list(self.connection.get_messages())
        new_messages = messages[self._last_msg_idx:]
        self._last_msg_idx = len(messages)
        return new_messages
    
    def _get_connection(self):
        return Connection(('localhost', 9090))
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._connection_provider(('localhost', 9090))
        return self._connection
    
    @connection.setter
    def connection(self, value):
        if self._connection is not None:
            self._connection.close()
        self._connection = value
        
    
        