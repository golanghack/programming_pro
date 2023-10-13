#! /usr/bin/env python3 

from typing import Any

class OrderedSimpleList:    
    """Class OrderedList:
            add -> add element in list,
            remove -> remove first found item from list, if 
            dont have an item in list genarate Exception
            ValueError
            __getitem__(index) -> return element for index from list(sortered)
            __contains__(item) -> return True, if element item in list
            __iter__ -> return iterator
            __len__ -> return lenght list 
    """
    
    def __init__(self): 
        self._lst = []
        
    def add(self, item: Any):
        self._lst.append(item)
        self._lst.sort()
        
    def remove(self, item: Any):
        self._lst.remove(item)
        
    def __getitem__(self, index: int) -> Any:
        return self._lst[index]
    
    def __contains__(self, item: Any) -> bool:
        left, right = 0, len(self._lst)
        while right - left > 1:
            median = (right + left) // 2
            if item < self._lst[median]:
                right = median
            else:
                left = median
        return right > left and self._lst[left] == item
    
    def __len__(self) -> int:
        return len(self._lst)
    
    def __iter__(self):
        return iter(self._lst)
    
    