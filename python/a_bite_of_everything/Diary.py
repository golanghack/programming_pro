#! /usr/bin/env python3 

class Diary:
    """Diary class il;ustrated encapsulation.
    
    >>> my_diary = Diary('Read')
    >>> my_diary.addentry('It')
    >>> print('Called ->', my_diary.title)
    Called -> Read
    """
    
    def __init__(self, title: str) -> None:
        self.title = title
        self._entries = []
        
    def addentry(self, entry: str) -> None:
        self._entries.append(entry)
        
    def _lastentry(self) -> str:
        return self._entries[-1]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()