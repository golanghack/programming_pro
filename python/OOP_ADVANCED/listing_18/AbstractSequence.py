#! /usr/bin/env python3 

from abc import ABCMeta, abstractmethod

class AbstractSequence(metaclass=ABCMeta):
    """Custom version collections.Sequence with abcstract base class""" 

    @abstractmethod
    def __len__(self):
        """Return the length of sequence""" 

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence""" 

    def __contains__(self, value):
        """Return True if value in the sequence; False otherwise""" 

        for j in range(len(self)):
            if self[j] == value:
                return True
            return False

    def index(self, value):
        """Return leftmost index at which value is found (or raise ValueError)""" 

        for j in range(len(self)):
            if self[j] == value:
                return j 
        raise ValueError('value not found in sequence')

    def count(self, value):
        """Return the number of elements equal to given value""" 

        k = 0 
        for j in range(len(self)):
            if self[j] == value:
                k += 1
        return k 

    