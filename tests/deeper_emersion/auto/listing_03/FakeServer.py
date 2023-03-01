#! /usr/bin/env python3 

from typing import Any

class FakeServer:
    
    def __init__(self):
        self.last_command = None
        self.last_args = None
        self.messages = []
        
    def __call__(self, *args, **kwargs):
        return self 
    
    def send(self, data: Any):
        callid, command, args, kwargs = data 
        self.last_command = command
        self.last_args = args
        
    def recv(self, *args, **kwargs):
        return '#ERROR', ValueError(f'{self.last_command} - {self.last_args!r}')
    
    def close(self):
        pass
    