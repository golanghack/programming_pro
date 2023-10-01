#! /usr/bin/env python3 

from minimal_custom_mapping import Entry
from typing import Any

class ListMappingSimple:
    
    def __init__(self):
        self._entries = []
        
    def put(self, key: Any, value: Any) -> None:
        for element in self._entries:
            if element.key == key:
                element.value = value
                return
        self._entries.append(Entry(key, value))
        
    def get(self, key: Any) -> Any or Exception:
        for element in self._entries:
            if element.key == key:
                return element.value
        raise KeyError