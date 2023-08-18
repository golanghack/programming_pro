#! /usr/bin/env python3

from LinkedListAdvance import LinkedList
from typing import Any 


class LinkedQueue:
    
    def __init__(self) -> None:
        self._queue = LinkedList()
        
    def enqueue(self, item: Any) -> None:
        self._queue.addlast(item)
        
    def dequeue(self) -> Any:
        return self._queue.removefirst()
    
    def peek(self) -> Any:
        item = self._queue.removefirst()
        self._queue.addfirst(item)
        return item
    
    def __len__(self) -> int:
        return len(self._queue)
    
    def isempty(self) -> bool:
        return len(self) == 0