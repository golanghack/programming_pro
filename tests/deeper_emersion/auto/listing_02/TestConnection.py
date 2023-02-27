#! /usr/bin/env python3 

import unittest

class TestConnection(unittest.TestCase):
    
    def test_broadcast(self):
        conn = Connection(('localhost', 9090))
        conn.broadcast('some message')
        
        assert conn.get_messages()[-1] == 'some message'