#! /usr/bin/env python3 

class AlterRange:
    """A class alter range (built-in range class)""" 

    def __init__(self, start, stop=None, step=1):
        """Initializing a AlterRange instance

        Semantics is similar to built-in range class
        """ 

        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start 
        self._size = max(0, (stop - start + step - 1) // step)
        # need knowledge of start and step -> __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range"""

        return self._size

    def __getitem__(self, index):
        """Return entry at index -> using standart interpratetiuon if negative"""

        if index < 0:
            # attempt to convert negative index
            index += len(self)
        if not 0 <= index < self._size:
            raise IndexError('index out of range')
        
        return self._start + index * self._step

        
