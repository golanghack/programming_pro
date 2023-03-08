#! /usr/bin/env python3 

import unittest
from unittest.mock import Mock
import io 
import threading
import queue
import tempfile
from pathlib import Path

from todo.app import TODOapp
from todo.db import BasicDB

class TestRegressions(unittest.TestCase):
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()
        
        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()
        
        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)
        
    def test_os_release(self):
        fake_file = io.StringIO()
        fake_file.close = Mock()
        
        data = ['buy milk', 'install "Focal Fossa"']
        
        dbmanager = BasicDB(None, _fileopener=Mock(return_value=fake_file))
        
        dbmanager.save(data)
        fake_file.seek(0)
        loaded_data = dbmanager.load()
        
        self.assertEqual(loaded_data, data)
            
unittest.main()

