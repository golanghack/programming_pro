#! /usr/bin/env python3 

class SimpleListPriorityQueue:
    """ 
    :param -> item 
    :param -> priority
    :method -> insert added element
    :method -> return minimal element
    :method -> removing and return minimal priority
    """

    def __init__(self):
        self._list_pq = []

    def insert(self, item, priority):
        self._list_pq.append((item, priority))

    def find_min(self):
        return min(self._list_pq, key=lambda x : x[1])[0]

    def remove_min(self):
        item, priority = min(self._list_pq, key=lambda x : x[1])
        self._list_pq.remove((item, priority))
        return item

class Entry:

    def __init__(self, item, priority):
        self.priority = priority 
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority

        