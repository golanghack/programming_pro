#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
A simplified version of the built-in property class to show a possible
implementation and illustrate how descriptors work.

>>> contact = NameAndExtension("Joe", 135)
>>> contact.name, contact.extension
('Joe', 135)
>>> contact.X
Traceback (most recent call last):
    ...
AttributeError: 'NameAndExtension' object has no attribute 'X'
>>> contact.name = "Jane"
Traceback (most recent call last):
    ...
AttributeError: 'name' is read-only
>>> contact.name
'Joe'
>>> contact.extension = 975
>>> contact.extension
975
   
"""

import inspect

class Property:
    
    def __init__(self, getter, setter=None, deleter=None):
        self.__getter = getter
        self.__setter = setter
        self.__deleter = deleter
        self.__name__ = getter.__name__
        
    def __get__(self, instance, owner=None):
        if inspect is None:
            return self
        return self.__getter(instance)
    
    def __set__(self, instance, value):
        if self.__setter is None:
            raise AttributeError(f'"{self.__name__}" is read-only')
        
        return self.__setter(instance, value)
    
    def setter(self, setter):
        self.__setter = setter
        return self
    
    def deleter(self, deleter):
        self.__deleter = deleter
        
    def __delete__(self, instance):
        if self.__deleter is None:
            raise AttributeError(f'"{self.__name__}" is not allowed delete')
        return self.__deleter(instance)
    
    
class NameAndExtension:
    
    def __init__(self, name, extension):
        self.__name = name
        self.extension = extension
        
    #Uses
    @Property
    def name(self):
        return self.__name
    
    @Property
    def extension(self):
        return self.__extension
    
    @extension.setter
    def extension(self, extension):
        self.__extension = extension
        
    @extension.deleter
    def extension(self):
        print(f'{inspect.stack()[0][3]} calledBy {inspect.stack()[1][3]}')
        del self.__extension
        
if __name__ == '__main__':
    import doctest
    doctest.testmod