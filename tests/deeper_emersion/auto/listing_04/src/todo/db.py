#! /usr/bin/env python3 

class BasicDB:
    
    def __init__(self, path: str, _fileopener=open):
        self._path = path 
        self._fileopener = _fileopener
        
        