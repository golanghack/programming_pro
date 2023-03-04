#! /usr/bin/env python3 

import functools
class TODOapp:
    
    def __init__(self, io=(input, functools.partial(print, end=''))):
        self._in, self._out = io 