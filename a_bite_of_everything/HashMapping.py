#! /usr/bin/env python3 

from minimal_custom_mapping import Entry
from ListMapping import ListMapping
from typing import Any

class HashMapping:
    
    def __init__(self, size: int=1) -> None:
        self._size = size
        self._buckets = [ListMapping() for element in range(self._size)]
        self._lenght = 0
        
    def _bucket(self, key: Any):
        return self._buckets[hash(key) % self._size]
    
    def _double(self):
        # save link on old container
        old_buckets = self._buckets
        
        # doubling
        self._size *= 2
        
        # create new containers
        self._buckets = [ListMapping() for element in range(self._size)]
        
        # added to all containers new record
        for bucket in old_buckets:
            for key, value in bucket.items():
                # identity new container
                new_backet = self._bucket(key)
                new_backet[key] = value
        
    def put(self, key: Any, value: Any) -> None:
        base = self._bucket(key)
        if key not in base:
            self._lenght += 1
        base[key] = value
        
        # conteiners add?
        if self._lenght > self._size:
            self._double()
            
    def get(self, key: Any) -> Any:
        base = self._bucket(key)
        return base[key]
    
    def remove(self, key: Any) -> None:
        base = self._bucket(key)
        base.remove(key)
        
    def __contains__(self, key: Any) -> bool:
        base = self._bucket(key)
        return key in base
    
    def __len__(self) -> int:
        return self._lenght
    
    def __iter__(self):
        for element in self._buckets:
            for k in element:
                yield k 
                
    def values(self):
        for element in self._buckets:
            for v in element.values():
                yield v 
                
    def items(self):
        for element in self._buckets:
            for key, value in element.items():
                yield key, value
                
    def __str__(self) -> str:
        # DUNGER!!! 
        # open close attribute
        item_list = [str(element) for base in self._buckets for element in base._entries]
        return '{' + ', '.join(item_list) + '}'
    
    __getitem__ = get
    __setitem__ = put
    
    