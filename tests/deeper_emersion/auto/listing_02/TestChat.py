#! /usr/bin/env python3 

import unittest
from ChatClient import ChatClient
from Connection import Connection
import unittest.mock

class TestChatAcceptance(unittest.TestCase):
    
    def test_message_exchange(self):
        user1 = ChatClient('JD')
        user2 = ChatClient('Hp')
        
        user1.send_message('Hello')
        messages = user2.fetch_messages()
        assert messages == ['JD -> Hello']
        
        
class TestChatClient(unittest.TestCase):
    
    def test_nickname(self):
        client = ChatClient('User 1')
        
        assert client.nickname == 'User 1'
        
    def test_send_message(self):
        client = ChatClient('User 1')
        client.connection = unittest.mock.Mock()
        sent_message = client.send_message('Hello')
        
        assert sent_message == 'User 1: Hello'
        
class TestConnection(unittest.TestCase):
    
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, 'connect'):
            conn = Connection(('localhost', 9090))
        
        with unittest.mock.patch.object(conn, 'get_messages', return_value = []):
            conn.broadcast('Some message')
            
            assert conn.get_messages()[-1] == 'Some message'
            
    def test_client_connection(self):
        client = ChatClient('User 1')
        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(client, '_get_connection', return_value=connection_spy):
            client.send_message('Hello')
            
        connection_spy.broadcast.assert_called_with('User 1: Hello')
        
if __name__ == '__main__':
    unittest.main()