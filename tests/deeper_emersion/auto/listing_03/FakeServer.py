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
        if self.last_command == 'dummy':
            return '#RETURN', None
        else:
            return '#ERROR', ValueError(f'{self.last_command} - {self.last_args}')
    
    def close(self):
        pass
    