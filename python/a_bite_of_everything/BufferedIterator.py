#! /usr/bin/env python3 

class BufferedIterator:
    
    def __init__(self, i: int):
        self._i = iter(i)
        self._hash_next = True
        self._buffer = None
        self._advance()
        
    def peek(self):
        return self._buffer
    
    def hash_next(self):
        return self.hash_next

    def _advance(self):
        try:
            self._buffer = next(self._i)
        except StopIteration:
            self._buffer = None
            self._hash_next = False
            
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.hash_next():
            output = self.peek()
            self._advance()
            return output
        else:
            raise StopIteration