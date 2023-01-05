#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--OPPORTUNIST-->"""

import sys 
import time

class Point:
    """Class building points"""
    
    __slots__ = ('x', 'y', 'z', 'color')
    
    def __init__(self, x: int=0, y: int=0, z: int=0, color: str=None) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        
    def __repr__(self) -> str:
        return f'Point({self.x!r}), {self.y!r}, {self.z!r}, {self.color!r})'
    
def main():
    regression = False
    size = int(1e6)
    if len(sys.argv) > 1 and sys.argv[1] == '-P':
        regression = True
        size = 20
    start = time.process_time
    ()
    points = []
    
    for i in range(size):
        points.append(Point(i, i ** 2, i // 2))
    end = time.process_time() - start
    assert points[size - 1].x == size - 1
    assert points[size - 1].color is None
    
    print(len(points))
    if not regression:
        print(f'took {end} secs to create {size,} points')
        input('press Enter to finish')
        
if __name__ == '__main__':
    main()