#! /usr/bin/env python3 

from ListStack import ListStack
from typing import Any

class AnotherStack(ListStack):
    
    def pop(self) -> Any:
        try:
            return self._stack.pop()
        except IndexError:
            raise RuntimeError('pop from empty stack')
        