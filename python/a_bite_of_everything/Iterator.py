#! /usr/bin/env python3 

class Iterator:
    
    def __init__(self):
        self._count = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count < 10:
            self._count += 1
            return self._count
        else:
            raise StopIteration
        
# testing
iterator_one = Iterator()
for index in iterator_one:
    print(index)

iterator_two = Iterator()
list_indexes = [2 * x for x in iterator_two]

