#! /usr/bin/env python3 

from SimpleListQueuePriority import Entry

class HeapPQ:

    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries) - 1)

    def _parent(self, i):
        return (i - 1) // 2

    def _children(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def find_min(self):
        return self._entries[0].item


    def remove_min(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._down_heap(0)
        return item

    
    def _down_heap(self, i):
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key=lambda x : L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._down_heap(child)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._down_heap(i)

    def _heapify_slower(self):
        n = len(self._entries)
        for i in range(n):
            self._upheap(i)
