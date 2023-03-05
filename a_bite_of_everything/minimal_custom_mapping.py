#! /usr/bin/env python3 

from typing import Any

class Entry:
    """MINIMAL CUSTOM MAPPING.
    Abstract structiure
    :param: -> get(k) where k - key
    return value for key. If value is not rause KeyError
    :param: -> put(k, v) where k - key, v - value
    added key-value in map.
    """
    
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        
    def __str__(self) -> str:
        return str(self.key) + ' : ' + str(self.value)
    
    def map_put(l: list, key: Any, value: Any) -> None:
        for element in l:
            if element.key == key:
                element.value = value
                return
        l.append(Entry(key, value))
        
    def map_get(l: list, key: Any) -> Any:
        for element in l:
            if element.key == key:
                return element.value
        raise KeyError
    
    
