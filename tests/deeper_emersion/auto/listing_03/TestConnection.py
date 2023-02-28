#! /usr/bin/env python3 

import unittest
from Connection import Connection 

class TestConnection(unittest.TestCase):
    
    def test_broadcast(self):
        conn = Connection(('localhost', 9090))
        conn.broadcast('message')
        
        assert conn.get_messages()[-1] == 'message'