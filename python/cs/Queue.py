#! /usr/bin/env python3 

from typing import Any

"""Queue -> queue on FIFO"""

class Queue(object):
    """ 
    >>> queue = Queue()
    >>> queue.enqueue('One')
    >>> queue.enqueue('Two')
    >>> queue.enqueue('Three')
    >>> print(queue.size())
    3
    >>> queue.dequeue()
    'One'
    >>> print(queue.size())
    2
    """ 

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []
    
    def enqueue(self, item: Any):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    import doctest
    doctest.testmod()