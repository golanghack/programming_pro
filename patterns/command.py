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
import Command

class Grid:
    
    def __init__(self, width: int, height: int) -> None:
        self.__cells = [['white' for _ in range(height)] for _ in range(width)]
        
    def cell(self, x: int, y: int, color: str=None):
        if color is None:
            return self.__cells[x][y]
        self.__cells[x][y] = color
        
    @property
    def rows(self) -> int:
        return len(self.__cells[0])
    
    @property
    def columns(self) -> int:
        return len(self.__cells)
    
class UndoableGrid(Grid):
    
    def create_cell_command(self, x: int, y: int, color: str):
        def undo():
            self.cell(x, y, undo.color)
        def do():
            undo.color = self.cell(x, y)
            self.cell(x, y, color)
        return Command.Command(do, undo, 'Cell')
    
def create_rectangle_macro(self, x0: int, y0: int, x1: int, y1: int, color: str):
    macro = Command.Macro('Rectangle')
    for x in range(x0, x1 + 1):
        macro.add(self.create_cell_command(x, y, color))
    return macro

