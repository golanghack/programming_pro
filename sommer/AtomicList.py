#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--ACID OPERATION WITH CUSTOM CLASS CONTECST-->"""

import copy

class AtomicList:
    
    def __init__(self, alist: list, shallow_copy: bool=True) -> None:
        self.original = alist
        self.shallow_copy = shallow_copy
        
    def __enter__(self):
        self.modified = (self.original[:] if self.shallow_copy else copy.deepcopy(self.original))
        return self.modified
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original[:] = self.modified
            
try:
    with AtomicList(items) as atomic:
        atomic.append(58289)
        del atomic[3]
        atomic[8] = 81738
        atomic[index] = 38172
except (AttributeError, IndexError, ValueError) as err:
    print('no change appied --> ', err)
    
    