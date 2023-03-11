#! /usr/bin/env python3 

from typing import Any

class BSTNode:
    
    def __init__(self, key:Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._lenght = 1
        
    def __len__(self) -> int:
        return self._lenght
    
    def __str__(self) -> str:
        return str(self.key) + ' -> ' + str(self.value)
    
    def get(self, key: Any) -> Any:
        if key == self.key:
            return self
        elif key < self.key and self.left:
            return self.left.get(key)
        elif key > self.key and self.right:
            return self.right.get(key)
        else:
            raise KeyError
        
    def put(self, key: Any, value: Any):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left:
                self.left.put(key, value)
            else:
                self.left = BSTNode(key, value)
        elif key > self.key:
            if self.right:
                self.right.put(key, value)
            else:
                self.right = BSTNode(key, value)
        self._update_lenght()
        
    def _update_lenght(self):
        len_left = len(self.left) if self.left else 0
        len_right = len(self.right) if self.right else 0 
        self._lenght = 1 + len_left + len_right
        
    def floor(self, key: Any):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left is not None:
                return self.left.floor(key)
            else:
                return None
        elif key > self.key:
            if self.right is not None:
                floor = self.right.floor(key)
                return floor if floor is not None else self
            else:
                return self
            
    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right
            
    def _swap_with(self, other):
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value
        
    def max_node(self):
        return self.right.max_node() if self.right else self
    
    def remove(self, key: Any):
        if key == self.key:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            self._swap_with(self.left.max_node())
            self.left = self.left.remove(key)
        elif key < self.key and self.left:
            self.left = self.left.remove(key)
        elif key > self.key and self.right:
            self.right = self.right.remove(key)
        else:
            raise KeyError
        self._update_lenght()
        return self
    

        
                