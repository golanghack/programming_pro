#! /usr/bin/env python3 

from minimal_custom_mapping import Entry
from typing import  Any

class ListMapping:
    
    def __init__(self):
        self._entries = []
        
    def put(self, key: Any, value: Any) -> None:
        element = self._entry(key)
        if element is not None:
            element.value = value
        else:
            self._entries.append(Entry(key, value))
            
    def get(self, key: Any) -> Any or Exception:
        element  = self._entry(key)
        if element is not None:
            return element.value
        else:
            raise KeyError
        
    def remove(self, key: Any) -> None:
        element = self._entry(key)
        if element is not None:
            self._entries.remove(element)
            
    def _entry(self, key: Any) -> Any or None:
        for element in self._entries:
            if element.key == key:
                return element
        return None
    
    def __str__(self) -> str:
        return '{' + ', '.join(str(element) for element in self._entries + '}')
    
    def __len__(self) -> int:
        return len(self._entries)
    
    def __contains__(self, key: Any) -> bool:
        if self._entry(key) is None:
            return False
        return True
    
    def __iter__(self) -> tuple:
        return (element.key for element in self._entries)
    
    def values(self) -> tuple:
        return (element.value for element in self._entries)
    
    def items(self) -> tuple:
        return ((element.key, element.value) for element in self._entries)
    
    __getitem__ = get
    __setitem__ = put 