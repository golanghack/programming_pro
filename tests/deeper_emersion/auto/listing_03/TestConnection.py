#! /usr/bin/env python3 

import unittest
import unittest.mock
from Connection import Connection 
from FakeServer import FakeServer

class TestConnection(unittest.TestCase):
    
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, 'connect'):
            conn = Connection(('localhost', 9090))
        with unittest.mock.patch.object(conn, 'get_messages', return_value=[]):
            conn.broadcast('message')
            
            assert conn.get_messages()[-1] == 'message'
            
    def test_exchange_with_server(self):
        with unittest.mock.patch(
            'multiprocessing.managers.listener_client', 
            new={'pickle': (None, FakeServer())}
        ):
            conn1 = Connection(('localhost', 9090))
            conn2 -= Connection(('localhost', 9090))
            
            conn1.broadcast('connected message')
            
            assert conn2.get_messages()[-1] == 'connected message'
unittest.main()