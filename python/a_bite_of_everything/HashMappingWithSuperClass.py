#! /usr/bin/env python3 

from Mapping import Mapping
from ListMapping import ListMapping

class HashMapping(Mapping):
    
    def __init__(self, size=100):
        self._size = size
        self._buckets = [ListMapping() for i in range(self._size)]
        self._lenght = 0
        
    
    def _entry_iter(self):
        return (element for bucket in self._buckets for element in bucket._entry_iter())
    
    def get(self, key):
        bucket = self._buckets(key)
        return bucket[key]
    
    def put(self, key, value):
        bucket = self._bucket(key)
        if key not in bucket:
            self._lenght += 1
        bucket[key] = value
        
        # added new containers?
        if self._lenght > self._size:
            self._double()
            
    def __len__(self):
        return self._lenght
    
    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]
    
    def _double(self):
        # save old containers 
        old = self._buckets
        # reinitialization old contaienrs and new containers
        self.__init__(self._size * 2)
        for bucket in old:
            for key, value in bucket.items():
                self[key] = value
                