#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GROUP OF CLASSES WITH METACLASSES-->"""

import collections

class LoadableSaveable(type):
    
    def __init__(cls, classname: str, bases: list, dictonary: dict) -> None:
        super().__init__(classname, bases, dictonary)
        assert hasattr(cls, 'load') and isinstance(getattr(cls, 'load'), collections.Callable), ('class"' + 
                                                                                                 classname + 
                                                                                                 '" my=ust provide a load() method')
        assert hasattr(cls, 'save') and isinstance(getattr(cls, 'save'), collections.Callable), ('class "' + 
                                                                                                 classname + '" must provide a save() method')
        
        