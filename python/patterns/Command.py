#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--COMMAND-->"""

class Command:
    
    def __init__(self, do, undo, description='') -> None:
        assert callable(do) and callable(undo)
        self.do = do
        self.undo = undo
        self.description = description
        
    def __call__(self):
        self.do()
    
class Macro:
    
    def __init__(self, description: str=''):
        self.description = description
        self.__commands = []
        
    def add(self, command: str) -> list:
        if not isinstance(command, Command):
            raise TypeError(f'Expected object of type Command, got {type(command).__name__}')
        self.__commands.append(command)
        
    def __call__(self):
        for command in self.__commands:
            command()
            
    do = __call__
    
    def undo(self):
        for command in reversed(self.__commands):
            command.undo()