#! /usr/bin/env python3 

import json
class BasicDB:
    
    def __init__(self, path: str, _fileopener=open):
        self._path = path 
        self._fileopener = _fileopener
        
    def load(self):
        try:
            with self._fileopener(self._path, 'r', encoding='utf-8') as file_:
                return json.load(file_)
        except FileNotFoundError:
            return []
        
    def save(self, values):
        with self._fileopener(self._path, 'w+', encoding='utf-8') as file_:
            file_.write(json.dumps(values))
            
    
    