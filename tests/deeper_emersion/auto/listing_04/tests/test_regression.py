#! /usr/bin/env python3 

import unittest
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
        with tempfile.TemporaryDirectory() as temp_dir:
            app_thead = threading.Thread(target=TODOapp(
                io=(self.fake_input, self.fake_output), 
                dbmanager=BasicDB(Path(temp_dir, 'db'))
            ).run, daemon=True)
            
            app_thead.start()
            self.get_output()
            
            self.send_input('add buy milk')
            self.send_input('add "Focal Fossa"')
            self.send_input('quit')
            app_thead.join(timeout=1)
            
            while True:
                try:
                    self.get_output()
                except queue.Empty:
                    break
                
            app_thead = threading.Thread(target=TODOapp(
                io=(self.fake_input, self.fake_output),
                dbmanager=BasicDB(Path(temp_dir, 'db'))
            ).run, daemon=True)
            app_thead.start()
            self.get_output()
            
unittest.main()

