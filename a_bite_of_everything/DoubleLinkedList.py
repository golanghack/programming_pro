#! /usr/bin/env python3 

from typing import Any

class DoubleLinkedListNode:
    """
    Realisation double linked list.
    data -> data
    prev -> link on last element
    link -> link on next element. 
    
    link pointer from begin to end indexes
    prev pointer from end to begin indexes
    """
    
    def __init__(self, data: Any, prev: str=None, link: str=None):
        self.data = data
        self.prev = prev
        self.link = link
        
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self
            
class DoubleLinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._lenght = 0 
        
    def add_first(self, item: Any) -> None:
        if len(self) == 0:
            self._head = self._tail = DoubleLinkedListNode(item, None, None)
        else:
            new_node = DoubleLinkedListNode(item, None, self._head)
            self._head.prev = new_node
            self._head = new_node
            self._lenght += 1
    
    def add_last(self, item: Any) -> None:
        if len(self) == 0:
            self._head = self._tail = DoubleLinkedListNode(item, None, None)
        else:
            new_node = DoubleLinkedListNode(item, self._tail, None)
            self._tail.link = new_node
            self._tail = new_node
        self._lenght += 1
        
    def __len__(self):
        return self._lenght