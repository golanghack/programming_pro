#! /usr/bin/env python3 

from multiprocessing.managers import SyncManager
from typing import Any
from FakeServer import *
class Connection(SyncManager):
    
    def __init__(self, address: str) -> None:
        self.register('get_messages')
        super().__init__(address=address, authkey=b'mychatsecret')
        self.connect()
        
    def broadcast(self, message: Any) -> list:
        messages = self.get_messages()
        messages.append(message)
        return messages
        

        