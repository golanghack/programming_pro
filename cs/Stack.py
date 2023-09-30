#! /usr/bin/env python3

from typing import Any
""" 
Create data struct Stack
""" 

class Stack:
    """FIFO Stack""" 

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def push(self, item: Any) -> list:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def peek(self) -> Any:
        return self.items[len(self.items) - 1]
    
    def size(self) -> int:
        return len(self.items)

        