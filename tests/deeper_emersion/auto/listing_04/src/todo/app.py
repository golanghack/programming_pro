#! /usr/bin/env python3 

import functools
class TODOapp:
    
    def __init__(self, io=(input, functools.partial(print, end=''))):
        self._in, self._out = io 
        self._quit = False
        
    def run(self):
        self._quit = False
        while not self._quit:
            self._out(self.prompt(''))
            command = self._in()
        self._out('buy!\n')
        
    def prompt(self, output):
        return f""" 
    TODOs:
    {output}
    > """