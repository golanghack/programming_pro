#! /usr/bin/env python3 

class Entry:
    def __init__(self, k, v):
        self.key = k 
        self.value = v

class Hashtable:
    """Show working a hash in python"""

    def __init__(self, M: int) -> None:
        self.table = [[] for i in range(M)]
        self.M = M 
        self.N = 0 

    def get(self, k: int) -> int or None:
        hc = hash(k) % self.M 
        for entry in self.table[hc]:
            if entry.key == k:
                return entry.value
        return None

    def put(self, k, v):
        hc = hash(k) % self.M 
        for entry in self.table[hc]:
            if entry.key == k:
                entry.value = v
                return
        self.table[hc].append(Entry(k, v))
        self.N += 1

    def remove(self, k):
        hc = hash(k) % self.M 
        for i, entry in enumerate(self.table[hc]):
            if entry.key == k:
                del self.table[hc][i]
                self.N -= 1 
                return entry.value
        return None 