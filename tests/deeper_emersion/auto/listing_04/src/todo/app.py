#! /usr/bin/env python3 

import functools
class TODOapp:
    
    def __init__(self, io=(input, functools.partial(print, end=''))):
        self._in, self._out = io 
        self._quit = False
        self._entries = []
        
    def run(self):
        self._quit = False
        while not self._quit:
            self._out(self.prompt(''))
            command = self._in()
            self._dispatch(command)
        self._out('buy!\n')
        
    def prompt(self, output):
        return f"""TODOs:
{output}

> """

    def _dispatch(self, cmd):
        cmd, *args = cmd.split('', 1)
        executor = getattr(self, f'cmd_{cmd}', None)
        if executor is None:
            self._out(f'Invalid command -> {cmd}')
            return
        executor(*args)
        
        
    def cmd_add(self, what):
        self._entries.append(what)
        