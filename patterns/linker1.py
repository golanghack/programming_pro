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

import abc 
import sys 


class AbstractItem(metaclass=abc.ABCMeta):
    
    @abc.abstractproperty
    def composite(self):
        pass
    
    def __iter__(self):
        return iter([])
    
class SimpleItem(AbstractItem):
    
    def __init__(self, name:str, price:float=0.00) -> None:
        self.name = name
        self.price = price
           
    @property
    def composite(self):
        return False
    
    def print_(self, indent:str='', file=sys.stdout) -> str:
        print(f'{indent}${self.price:.2f} {self.name}', file=file)

class AbstractCompositeItem(AbstractItem):
    
    def __init__(self, *items: str) -> None:
        self.children = []
        if items:
            self.add(*items)
            
    def add(self, first: str, *items: str) -> None:
        self.children.append(first)
        if items:
            self.children.extend(items)
            
    def remove(self, item: str) -> None:
        self.children.remove(item)
        
    def __iter__(self):
        return iter(self.children)
    
    
class CompositeItem(AbstractCompositeItem):
    
    def __init__(self, name: str, *items: str) -> None:
        super().__init__(*items)
        self.name = name
        
    @property
    def composite(self):
        return True
    
    @property
    def price(self) -> float:
        return sum(item.price for item in self)
    
    def print_(self, indent:str='', file=sys.stdout) -> str:
        print(f'{indent}{self.price:.2f} {self.name}', file=file)
        for child in self:
            child.print_(indent + '      ')
            
def main():
    pencil = SimpleItem('Pencil', 0.40)
    ruler = SimpleItem('ruler', 1.60)
    eraser= SimpleItem('Eraser', 0.20)
    pencilSet = CompositeItem('Pencil Set', pencil, ruler, eraser)
    box = SimpleItem('Box', 1.00)
    boxedPencilSet = CompositeItem('Boxed Pencil Set', box, pencilSet)
    boxedPencilSet.add(pencil)
    for item in (pencil, ruler, pencilSet, boxedPencilSet):
        item.print_()
          
    
if __name__ == '__main__':
    main()