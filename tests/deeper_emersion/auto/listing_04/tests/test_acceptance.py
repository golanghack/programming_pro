#! /usr/bin/env python3

import unittest
import threading
import queue
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
        
        self.send_input('quit')
        app_thead.join(timeout=1)
        
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
        
        self.assertEqual(self.get_output(), 'bye!\n')
        
if __name__ == '__main__':
    unittest.main()