#! /usr/bin/env python3 

class SequenceIterator:
    """An iterator for sequence"""

    def __init__(self, sequence: list) -> None:
        """Create an iterator for the sequence"""

        self._seq = sequence
        self._index = -1 

    def __next__(self):
        """Return next item or StopIteration raise""" 
        self._index += 1
        if self._index < len(self._seq):
            return (self._seq[self._index])
        else:
            raise StopIteration()

    def __iter__(self):
        """Convertion an iterator must return itself as an iterator""" 

        return self
        