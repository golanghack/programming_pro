#! /usr/bin/env python3 
from typing import Any
from ListQueueFakeDelete import ListQueueFakeDelete

class ListQueue(ListQueueFakeDelete):
    
    def dequeue(self) -> Any:
        item = self._queue[self._head]
        self._head += 1
        if self._head > len(self._queue) // 2:
            self._queue = self._queue[self._head:]
            self._head = 0
        return item
    
    