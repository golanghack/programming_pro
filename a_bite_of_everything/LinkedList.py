#! /usr/bin/env python3 

from typing import Any
from ListNode import ListNode

class LinkedList:
    
    def __init__(self):
        self._head = None
        
    def addfirst(self, item: Any) -> None:
        self._head = ListNode(item, self._head)
        
    def removefirst(self) -> Any:
        item = self._head.data 
        self._head = self._head.link
        return item 
    
    