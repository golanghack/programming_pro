#! /usr/bin/env python3 

from SimpleListQueuePriority import Entry 
from HeapPriorityQueue import HeapPQ

class PriorityQueue(HeapPQ):

    def __init__(self, items = (), entries = (), key=lambda x : x):
        self._key = key
        self._entries = [Entry(i, p) for i, p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._item_map = {entry.item : index for index, entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority=None):
        if priority is None:
            priority = self._key(item)
        index = len(self._entries)
        self._entries.append(Entry(item, priority))
        self._item_map[item] = index
        self._upheap(index)

    def _swap(self, a, b):
        L = self._entries
        value_a = L[a].item
        value_b = L[b].item

        self._item_map[value_a] = b
        self._item_map[value_b] = a
        L[a], L[b] = L[b], L[a]


    def change_priority(self, item, priority=None):
        if priority is None:
            priority = self._key(item)
        i = self._item_map[item]
        self._entries[i].priority = priority

        # is ordered heap
        self._upheap(i)
        self._down_heap(i)

    def remove_min(self):
        L = self._entries
        item = L[0].item
        self._swap(0, len(L) - 1)
        del self._item_map[item]
        L.pop()
        self._down_heap(0)
        return item

    