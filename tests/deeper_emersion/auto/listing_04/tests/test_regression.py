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
        
        app = TODOapp(
            io=(Mock(side_effect=['add buy milk', 'add install "Focal Fossa"', 'quit']), 
                Mock()),
            dbmanager=BasicDB(None, _fileopener=Mock(side_effect=[
                FileNotFoundError, 
                fake_file,
            ]))
        )
        app.run()
        
        fake_file.seek(0)
        
        restarted_app = TODOapp(
            io=(Mock(return_value='quit'), Mock()),
            dbmanager=BasicDB(None, _fileopener=Mock(return_value=fake_file))
        )
        
        restarted_app.run()
            
unittest.main()

