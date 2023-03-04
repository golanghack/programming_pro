#! /usr/bin/env python3

import unittest
import threading

class TestTODOAcceptance(unittest.TestCase):
    
    def test_main(self):
        app = TODOapp(io=(self.fake_input, self.fake_output))
        
        app_thead = threading.Thread(target=app.run, daemon=True)
        app_thead.start()
        
        welcome = self.get_output()
        self.assertEqual(welcome, ('TODOs:\n'
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