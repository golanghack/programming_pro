#! /usr/bin/env python3 

class Mapping:
    # class child must be build this method 
    def get(self, key):
        raise NotImplementedError
    
    def put(self, key, value):
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError
    
    def _entry_iter(self):
        raise NotImplementedError
    
    def __iter__(self):
        return (element.key for element in self._entry_iter())
    
    def values(self):
        return (element.value for element in self._entry_iter())
    
    def items(self):
        return ((element.key, element.value) for element in self._entry_iter())
    
    def __contains__(self, key):
        try:
            self.get(key)
        except KeyError:
            return False
        return True
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
        
    def __str__(self) -> str:
        return '{' + ', '.join(str(element) for element in self._entry_iter()) + '}'
    
    