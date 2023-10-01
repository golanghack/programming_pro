#! /usr/bin/env python3 

""" 
Problem 

You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.

EXAMPLE->

    >>> class Item:
           def __init__(self, name):
               self.name = name 

            def __repr__(self):
                return f'Item({self.name!r})
    >>> import PriorityQueue
    >>> q = PriorityQueue()
    >>> q.push(Item('foo'), 1)
    >>> q.push(Item('bar'), 5)
    >>> q.push(Item('spam'), 4)
    >>> q.push(Item('grok'), 1)
    >>> q.pop()
    Item('bar')
    >>> q.pop()
    Item('spam')
    >>> q.pop()
    Item('foo')
    >>> q.pop()
    Item('grok')
"""
import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0 

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()