#! /usr/bin/env python3

import unittest
from pathlib import Path
from unittest.mock import Mock
import threading
import queue
import tempfile
from todo.app import TODOapp

class TestTODOAcceptance(unittest.TestCase):
    
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()
        
        self.fake_output = lambda txt: self.outputs.put(txt)
        self.send_input = lambda cmd: self.inputs.put(cmd)
        self.fake_input = lambda: self.inputs.get()
        self.get_output = lambda: self.outputs.get(timeout=1)
        
    def test_main(self):
        app = TODOapp(io=(self.fake_input, self.fake_output))
        
        app_thead = threading.Thread(target=app.run, daemon=True)
        app_thead.start()
        
        welcome = self.get_output()
        self.assertEqual(welcome, (
            'TODOs:\n'
            '\n'
            '\n'
            '> '
            ))
        
        self.send_input('add buy milk')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            'TODOs:\n'
            '1. buy milk\n'
            '\n'
            '> '
        ))
        
        self.send_input('add buy eggs')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            'TODOs:\n'
            '1. buy milk\n'
            '2. buy eggs\n'
            '\n'
            '> '
        ))
        
        self.send_input('del 1')
        welcome = self.get_output()
        self.assertEqual(welcome, (
            'TODOs:\n'
            '1. buy eggs\n'
            '\n'
            '> '
        ))
        
    def test_load(self):
        dbpath = Path(tempfile.gettempdir(), 'something')
        dbmanager = Mock(load=Mock(return_value=['buy bread', 'buy water']))
        app = TODOapp(io=(Mock(return_value='quit'), Mock()), dbpath=dbpath, dbmanager=dbmanager)
        app.run()
        
        dbmanager.load.assert_called_with(dbpath)
        assert app._entries == ['buy bread', 'buy water']
        
    def test_persistance(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_thread = threading.Thread(target=TODOapp(
                io=(self.fake_input, self.fake_output), 
                dbpath=temp_dir,
            ).run,
            daemon=True)
            app_thread.start()
            
            welcome = self.get_output()
            self.assertEqual(welcome, (
                'TODOs:\n'
                '\n'
                '\n'
                '> '
            ))
            
            self.send_input('add buy bread')
            self.send_input('quit')
            
            app_thread.join(timeout=1)
            
            while True:
                try:
                    self.get_output()
                except queue.Empty:
                    break
            
        
if __name__ == '__main__':
    unittest.main()