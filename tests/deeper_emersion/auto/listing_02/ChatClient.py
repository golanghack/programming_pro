#! /usr/bin/env python3 
from Connection import Connection
class ChatClient:
    
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        
    def send_message(self, message: str) -> str:
        sent_message = f'{self.nickname}: {message}'
        self.connection.broadcast(message)
        return sent_message
    
    def _get_connection(self):
        return Connection(('localhost', 9090))