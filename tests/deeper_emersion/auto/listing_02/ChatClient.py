#! /usr/bin/env python3 
from Connection import Connection
class ChatClient:
    
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self._connection = None
        
    def send_message(self, message: str) -> str:
        sent_message = f'{self.nickname}: {message}'
        self.connection.broadcast(message)
        return sent_message
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._get_connection()
        return self._connection
    
    @connection.setter
    def connection(self, value: str):
        if self._connection is not None:
            self._connection.close()
        self._connection = value
        
    def _get_connection(self):
        return Connection(('localhost', 9090))