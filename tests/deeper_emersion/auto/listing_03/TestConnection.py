#! /usr/bin/env python3 

import unittest
import unittest.mock
from Connection import Connection 

class TestConnection(unittest.TestCase):
    
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, 'connect'):
            conn = Connection(('localhost', 9090))
        with unittest.mock.patch.object(conn, 'get_messages', return_value=[]):
            conn.broadcast('message')
            
            assert conn.get_messages()[-1] == 'message'
            
unittest.main()