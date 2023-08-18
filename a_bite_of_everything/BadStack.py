#! /usr/bin/env python3 

from ListStack import ListStack
from typing import Any

class BadStack(ListStack):
    """Illustrated bad use oop and data structure."""
    
    def push(self, item: Any) -> None:
        self._stack.insert(0, item)
        
    def pop(self) -> Any:
        return self._stack.pop(0)
    
    def peek(self) -> Any:
        return self._stack[0]