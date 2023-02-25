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
        
    def __len__(self):
        return self._lenght
    
    def _add_between(self, item: Any, before, after):
        node = DoubleLinkedListNode(item, before, after)
        
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._lenght += 1
        
    def add_first(self, item):
        self._add_between(item, None, self._head)
        
    def add_last(self, item):
        self._add_between(item, self._tail, None)
        
    def _remove(self, node: DoubleLinkedListNode):
        before, after = node.prev, node.link
        
        if node is self._head:
            self._head = after
        else:
            before.link = after
        
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._lenght -= 1
        return node.data
    
    def remove_first(self):
        return self._remove(self._head)
    
    def remove_last(self):
        return self._remove(self._tail)
        

    # union two doublelinkedlist
    def __iadd__(self, other: list):
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail 
            self._lenght = self._lenght + other._lenght
            #cleanin other list
            other.__init__()
        return self
    
    