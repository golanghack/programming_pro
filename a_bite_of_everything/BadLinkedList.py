#! /usr/bin/env python3 

from typing import Any 
from ListNode import ListNode

class LinkedList:
    
    def __init__(self) -> None:
        self._head = None
        
    def addfirst(self, item: Any) -> None:
        self._head = ListNode(item, self._head)
        
    def addlast(self, item: Any) -> None:
        if self._head is None:
            self.addfirst(item)
        else:
            current_node = self._head
            while current_node.link is not None:
                current_node = current_node.link
            current_node.link = ListNode(item)
            
    def removefirst(self) -> Any:
        item = self._head.data
        self._head = self._head.link
        return item
    
    def removelast(self) -> Any:
        if self._head.link is None:
            return self.removefirst()
        else:
            current_node = self._head
            while current_node.link.link is None:
                current_node = current_node.link
            item = current_node.link.data
            current_node.link = None
            return item
            