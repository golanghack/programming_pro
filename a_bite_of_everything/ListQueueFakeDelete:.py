#! /usr/bin/env python3 

from typing import Any

class ListQueueFakeDelete:
    
    def __init__(self) -> None:
        self._head = 0
        self._queue = []
        
    def enqueue(self, item: Any) -> None:
        self._queue.append(item)
        
    def dequeue(self) -> Any:
        item = self.peek()
        self._head += 1
        return item
    
    def peek(self) -> Any:
        return self._head[self._head]
    
    def __len__(self):
        return len(self._queue) - self._head
    
    def isempty(self) -> bool:
        return len(self) == 0
    
    