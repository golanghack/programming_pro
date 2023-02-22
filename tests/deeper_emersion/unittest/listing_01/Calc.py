#! /usr/bin/env python3 

class Calc(object):
    
    def add(self, x, y):
        return x + y 
    
if __name__ == '__main__':
    calc = Calc()
    result = calc.add(3, 3)
