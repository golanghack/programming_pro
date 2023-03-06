#! /usr/bin/env python3 

import unittest
import tempfile
from pathlib import Path
from todo.app import TODOapp

class TestTODOapp(unittest.TestCase):
    
    def test_default_dbpath(self):
        app = TODOapp()
        assert Path('.').resolve() == Path(app._dbpath).resolve()
        
    def test_accepts_dbpath(self):
        expected_path = Path(tempfile.gettempdir(), something)
        app = TODOapp(dbpath=str(expected_path))
        assert expected_path == Path(app._dbpath)
        
unittest.main()