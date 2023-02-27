#! /usr/bin/env python3 

from _DummyConnection import _DummyConnection
class ChatClient:
    
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        
    def send_message(self, message: str) -> str:
        sent_message = f'{self.nickname}: {message}'
        self.connection.broadcast(message)
        return sent_message