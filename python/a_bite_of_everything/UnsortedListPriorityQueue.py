#! /usr/bin/env python3 

from SimpleListQueuePriority import Entry

class UnsortedListPriorityQueue:

    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
    
    def find_min(self):
        return min(self._entries).item

    def remove_min(self):
        entry = min(self._entries)
        self._entries.remove(entry)
        return entry.item   