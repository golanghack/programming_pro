#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--LINKER PATTERN ILLUSTRRATED-->"""

import itertools
import sys 

class Item:
    
    def __init__(self, name:str, *items:str, price:float=0.00) -> None:
        self.name = name
        self.price = price
        self.children = []
        if items:
            self.add(*items)
            
            
    @classmethod
    def create(Class, name:str, price:float):
        return Class(name, price=price)
    
    @classmethod
    def compose(Class, name, *items):
        return Class(name, *items)
    
    @property
    def composite(self):
        return bool(self.children)
    
    def add(self, first:str, *items:str) -> list:
        self.children.extend(itertools.chain((first,), items))
        
    def remove(self, item):
        self.children.remove(item)
        
    def __iter__(self):
        return iter(self.children)
    
    @property
    def price(self):
        return (sum(item.price for item in self) if self.children else self.__price)
    
    @price.setter
    def price(self, price:float) -> float:
        self.__price = price
        
    def print_(self, indent:str='', file=sys.stdout):
        print(f'{indent} {self.price:.2f} {self.name}', file=file)
        for child in self:
            child.print_(indent + '      ')
            
def make_item(name:str, price:float):
    return Item(name, price=price)

def make_composite(name, *items):
    return Item(name, *items)

def main():
    pencil = Item.create('Pencil', 0.40)
    ruler = Item.create('Ruler', 1.60)
    eraser = make_item('Eraser', 0.20)
    pencilSet = Item.compose('Pencil Set', pencil, ruler, eraser)
    box = Item.create('Box', 1.60)
    boxedPencilSet = make_composite('Boxed Pencil Set', box, pencilSet)
    boxedPencilSet.add(pencil)
    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print_()
    assert not pencil.composite
    pencil.add(eraser, box)
    assert pencil.composite
    pencil.print_()
    pencil.remove(eraser)
    assert pencil.composite
    pencil.remove(box)
    assert not pencil.composite
    pencil.print_()
    
if __name__ == '__main__':
    main()