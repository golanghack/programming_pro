#! /usr/bin/env python3 

from SimpleListQueuePriority import Entry

class SortedListPriorityQueue:

    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort(reverse=True)

    def find_min(self):
        return self._entries[-1].item

    def remove_min(self):
        return self._entries.pop().item