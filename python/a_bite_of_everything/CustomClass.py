#! /usr/bin/env python3 

from typing import Any

class Foo:
    
    def __init__(self, a: Any, b: Any, c: Any) -> None:
        self.a = a
        self.b = b 
        self.c = c
        
    def __lt__(self, other: Any) -> bool:
        return other.b < self.b
    
    def __str__(self) -> str:
        return f'{self.a} - {self.b} - {self.c}'
    
    def get_a(self):
        return self.a
    
