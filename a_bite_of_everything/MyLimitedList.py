#! /usr/bin/env python3 

from typing import Any

class MyLimitedList:
    """Custom limited list -> from base list class.
    
    >>> my_list = MyLimitedList()
    >>> my_list.append(1)
    >>> my_list.append(10)
    >>> my_list.append(100)
    >>> print(my_list[2])
    100
    """
    
    def __init__(self) -> None:
        self._L = []
        
    def append(self, item: Any) -> None:
        self._L.append(item)
        
    def __getitem__(self, index: int) -> Any:
        return self._L[index]
    
    
def test_my_limited_list() -> list:
    my_list = MyLimitedList()
    my_list.append(0)
    my_list.append(0)
    my_list.append(0)
    my_list.append('a')
    
    assert(my_list[0] == 0)
    assert(my_list[1] == 0)
    assert(my_list[2] == 0)
    assert(my_list[3] == 'a')
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()