#! /usr/bin/env python3 

from typing import Any, List 

class ListStack:
    """Class List Stack
    implementation of the stack abstract structure.
    
    methods:
            push -> added new element
            pop  -> delete new element (LIFO pattern)
            peek -> return last element (LIFO pattern)
            size -> return count elements in stack (alt special method len)
         isempty -> boolean functioality (True if is elemets in steck or False)
    """
    
    def __init__(self, item: Any) -> None:
        self._stack = []
        
    def push(self, item: Any) -> None:
        self._stack.append(item)
        
    def pop(self) -> Any:
        return self._stack.pop()
    
    def peek(self) -> Any:
        return self._stack[-1]
    
    def __len__(self) -> int:
        return len(self._stack)
    
    def isempty(self) -> bool:
        return len(self) == 0
    
    