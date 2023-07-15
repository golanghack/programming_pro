#! /usr/bin/env python3 

class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v 

class Hashtable:
    def __init__(self, M=10):
        # create list fo M-objects
        self.table = [None] * M 
        self.M = M 
        self.N = 0 

    def get(self, k):
        # number place from key k
        hash_get = hash(k) % self.M
        while self.table[hash_get]:
            if self.table[hash_get].key == k:
                return self.table[hash_get].value
            hash_get = (hash_get + 1) % self.M 
        return None

    def put(self, k, v):
        hash_get = hash(k) % self.M 
        while self.table[hash_get]:
            if self.table[hash_get].key == k:
                self.table[hash_get].value = v 
                return
            hash_get = (hash_get + 1) % self.M 
        if self.N >= self.M -1:
            raise RuntimeError ('Table is full')
        self.table[hash_get] = Entry(k, v)
        self.N += 1
        