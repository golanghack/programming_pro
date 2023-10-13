#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--MODULE ACCOUNT-->

>>> from Account import Transaction
>>> t = Transaction(300, '22-22-02', 'usd', 1.2, 'little desc')
>>> t
Transaction (300 '22-22-02''usd'1.2'little desc')

"""
class Transaction:
    
    def __init__(self, summ: float, date: str, currency: str, course: float, desc: str) -> None:
        
        self.amount = summ 
        self.date = date
        self.currency = currency
        self.course = course
        self.desc = desc
    
    @property    
    def __amount__(self) -> float:
        return self.amount
    
    @property
    def __date__(self) -> str:
        return self.date
    
    @property
    def __currency__(self) -> str:
        return self.currency
    
    @property
    def __rate__(self):
        return self.course
    
    @property
    def __usd__(self) -> float:
        return self.amount * self.course
    
    @property
    def __desc__(self) -> str:
        return self.desc
    
    def __repr__(self) -> str:
        return f'Transaction ({self.amount!r} {self.date!r}{self.currency!r}{self.course!r}{self.desc!r})'
        
    def __str__(self) -> str:
        pass
    
        

