#! /usr/bin/env python3 

from typing import Any

class ListDeq:
    """ 
    Abstract type structure -> Deq.
    
    methods:
            addfirst(item) -> added element item in begin deq
            addlast(item)  -> added element item in end deq
        removefirst(item)  -> remove first element item and return from deq
        removelast         -> remove last element item and return from deq
            len            -> return ciiunt elements in deq.
        """

    def __init__(self) -> None:
        self._deq = []
        
    def addfirst(self, item: Any) -> Any:
        self._deq.insert(0, item)
        
    def addlast(self, item: Any) -> Any:
        self._deq.append(item)
        
    def removefirst(self) -> Any:
        return self._deq.pop()
    
    def removelast(self) -> Any:
        return self._deq.pop()
    
    def __Len__(self) -> int:
        return len(self._deq)
        
        