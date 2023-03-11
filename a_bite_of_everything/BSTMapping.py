#! /usr/bin/env python3 

from Mapping import Mapping
from typing import Any

class BTSMapping(Mapping):
    """Binary Tree Mapping
    
    :param v -> value
    :param k -> key
    :method get(k)     -> return value from key (k) or KeyError
    :method put(k, v)  -> added key-value (k, v) in mapping
    :method floor(k)   -> return (k, v) for key-value
    :method remove(k)  -> remove value for k
    """
    
    def __init__(self):
        self._root = None
        
    def get(self, key: Any) -> Any or Exception:
        if self._root:
            return self._root.get(key).value
        raise KeyError
    
    def put(self, key: Any, value: Any) -> None:
        if self._root:
            self.root = self._root.put(key, value)
        else:
            self._root = BSTNode(key, value)
            
    def __len__(self) -> int:
        return len(self._root) if self._root is not None else 0 
    
    def _entry_iter(self):
        if self._root:
            yield from self._root
            
    def floor(self, key: Any) -> tuple:
        if self._root:
            floor_node = self._root.floor(key)
            if floor_node is not None:
                return (floor_node.key, floor_node.value,)
        return (None, None,)
    
    def remove(self, key: Any):
        if self._root:
            self._root = self._root.remove(key)
        else:
            raise KeyError
        
    def __delitem__(self, key: Any):
        self.remove(key)
    