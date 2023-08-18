#! /usr/bin/env python3 

from typing import Any

class ListQueueSimple:
    """Implementation of the abstract data struct type queue.
    
            Parameters of realisation.
            enqueue(item) -> added new element in queue,
            dequeue()     -> delete and return element (LIFO pattern),
            peek()        -> return last element (LIFO pattern), 
            __len__()     -> return size of queue, 
            isempty()     -> boolean functionality (True is empty or False).
    """
    
    def __init__(self) -> None:
        self._queue = []
        
    def enqueue(self, item: Any) -> None:
        self._queue.append(item)
        
    def dequeue(self) -> Any:
        return self._queue.pop(0)
    
    def peek(self) -> Any:
        return self._queue[0]
    
    def __len__(self) -> int:
        return len(self._queue)
    
    def isempty(self) -> bool:
        return len(self) == 0
        