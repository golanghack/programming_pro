#! /usr/bin/env python3 

from typing import Any 
from ListNode import ListNode

class LinkedList:
    
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._lenght = 0
        
    def addfirst(self, item: Any) -> None:
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._lenght += 1
        
    def addlast(self, item: Any) -> None:
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._lenght += 1
            
    def removefirst(self) -> Any:
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._lenght -= 1
        return item
    
    def removelast(self) -> Any:
        if self._head is self._tail:
            return self.removefirst()
        else:
            current_node = self._head
            while current_node.link is not self._tail:
                current_node = current_node.link
            item = self._tail.data 
            self._tail = current_node
            self._tail.link = None
            self._lenght -= 1
            return item 
        
    def __len__(self):
        return self._lenght
            