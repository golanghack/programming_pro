#! /usr/bin/env python3

import sys
import os

"""<--METAFINDER - import modules  .hy"""

class MetaLoader(object):
    """MetaLoader is object used for download modules witj .hy"""
    
    def __init__(self, path: str) -> None:
        self.path = path
        
    def is_package(self, fullname: str) -> bool:
        """Testing name and directory files is packages."""
        
        dirpath = '/'.join(fullname.split('.'))
        for pth in sys.path:
            pth = os.path.abspath(pth)
            composed_path = f'{pth}/{dirpath}/__init__.hy'
            if os.path.exists(composed_path):
                return True
        return False
    
    def load_module(self, fullname: str):
        """Loading module with name fullname,"""
        
        if fullname in sys.modules:
            return sys.modules[fullname]
        
        if not self.path:
            return
        sys.modules[fullname] = None
        mod = import_file_to_module(fullname, self.path)
        is_pkg = self.is_package(fullname)
        
        mod.__file__ = self.path
        mod.__loader__ = self
        mod.__name__ = fullname
        
        if is_pkg:
            mod.__path__ = []
            mod.__package__ = fullname
        else:
            mod.__package__ = fullname.rpartition('.')[0]
            
        sys.modules[fullname] = mod 
        return mod
    

class MetaImporter(object):
    """Meta import files with .hy"""
    
    def find_on_path(self, fullname: str) -> str:
        """fina and return compossed path for module."""
        
        file_system = ['%s/__init__.hy', '%s.hy']
        directory_path = '/'.join(fullname.split('.'))
        
        for pth in sys.path:
            pth = os.path.abspath(pth)
            for file_path in file_system:
                composed_path = file_path % (f'{pth}/{directory_path}')
                if os.path.exists(composed_path):
                    return composed_path
                
    def find_module(self, fullname: str, path: str=None):
        """ Return Metaloader with argument path."""
        
        path = self.find_on_path(fullname)
        if path:
            return MetaLoader(path)
        
sys.meta_path.append(MetaImporter())