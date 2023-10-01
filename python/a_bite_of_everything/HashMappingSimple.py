#! /usr/bin/env python3 

from ListMapping import ListMapping
from typing import Any

class HashMappingSimple:
    
    def __init__(self):
        self._size = 100
        self._buckets = [ListMapping() for element in range(self._size)]
        
    def put(self, key: Any, value: Any) -> None:
        base = self._bucket(key)
        base[key] = value
        
    def get(self, key: Any) -> Any:
        base = self._bucket(key)
        return base[key]
    
    def _bucket(self, key: Any):
        return self._buckets[hash(key) % self._size]
    
    