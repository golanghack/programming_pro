#! /usr/bin/env python3 

from typing import Any
from Connection import Connection

class ChatClient:
    
    def __init__(self, nickname: str):
        self.nickname = nickname
        
    def send_message(self, message: Any) -> str:
        sent_message = f'{self.nickname}: {str(message)}'
        self.connection.broadcast(message)
        return sent_message
    
    
        