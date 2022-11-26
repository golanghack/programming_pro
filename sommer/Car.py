#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CAR CLASS-->"""

"""Class Car
 wins -> count wins
 sits -> count sits
 mark -> name of mark
 prod -> name of produnction
 """
 
class Car:
    
    def __init__(self, wins=4, sits=5, mark='Subaru', prod='Japan'):
        """A Car characteristic
        
        >>> car = Car(4, 5, 'Subaru', 'Japan')
        >>> car
        Car (4, 5, 'Subaru', 'Japan')
        """
        
        self.wins = wins
        self.sits = sits
        self.mark = mark
        self.prod = prod 
        
    def __repr__(self):
        return f'Car ({self.wins!r}, {self.sits!r}, {self.mark!r}, {self.prod!r})'
            
    def __str__(self):
        return f'(wins -> {self.wins}), (sits -> {self.sits}), (mark -> {self.mark}), (prod -> {self.prod}'
    
    
class Wolcwagen(Car):
    
    def __init__(self, condo=True, wins=4, sits=4, mark='WW', prod='De'):
        """A Wolcwagen class 
        >>> ww = Wolcwagen()
        >>> ww
        Car (4, 4, 'WW', 'De')
        """
        
        super().__init__(wins, sits, mark, prod)
        self.condo = condo
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()