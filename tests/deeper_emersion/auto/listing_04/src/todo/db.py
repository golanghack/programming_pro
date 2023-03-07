#! /usr/bin/env python3 

class BasicDB:
    
    def __init__(self, path: str, _fileopener=open):
        self._path = path 
        self._fileopener = _fileopener
        
    def load(self):
        with self._fileopener(self._path, 'r', encoding='utf-8') as file_:
            txt = file_.read()
        return eval(txt)
    
    