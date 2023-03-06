#! /usr/bin/env python3 

import functools
class TODOapp:
    
    def __init__(self, io=(input, 
                           functools.partial(print, end='')), 
                            dbpath=None, 
                            dbmanager=None):
        self._in, self._out = io 
        self._quit = False
        self._entries = []
        self._dbpath = dbpath or '.'
        self._dbmanager = dbmanager
        
    def run(self):
        if self._dbmanager is not None:
            self._entries = self._dbmanager.load(self._dbpath)
            
        self._quit = False
        while not self._quit:
            self._out(self.prompt(self.items_list()))
            command = self._in()
            self._dispatch(command)
        self._out('buy!\n')
        
    def prompt(self, output):
        return f"""TODOs:
{output}

> """

    def _dispatch(self, cmd):
        cmd, *args = cmd.split(' ', 1)
        executor = getattr(self, f'cmd_{cmd}', None)
        if executor is None:
            self._out(f'Invalid command -> {cmd}')
            return
        executor(*args)
        
        
    def cmd_add(self, what):
        self._entries.append(what)
        
    def cmd_quit(self, *_):
        self._quit = True
        
    def cmd_del(self, idx):
        idx = int(idx) - 1
        if idx < 0 or idx >= len(self._entries):
            self._out('Invalid index\n')
            return
        self._entries.pop(idx)
        
    def items_list(self):
        enumerated_items = enumerate(self._entries, start=1)
        return '\n'.join(
            '{}. {}'.format(idx, entry) for idx, entry in enumerated_items
        )
        