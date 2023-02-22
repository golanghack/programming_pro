#! /usr/bin/env python3 

class Calc(object):
    
    def add(self, x: int, y: int) -> int:
        if type(x) != int and type(y) != int:
            raise TypeError(f'Invalid type -> {type(x)} and {type(y)}')
        return x + y
    
if __name__ == '__main__':
    calc = Calc()
    result = calc.add(3, 3)
