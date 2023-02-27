#! /usr/bin/env python3 

import unittest
from ChatClient import ChatClient
from Connection import Connection
from FakeServer import FakeServer
import unittest.mock

class TestChatAcceptance(unittest.TestCase):
    
    def test_message_exchange(self):
        user1 = ChatClient('JD')
        user2 = ChatClient('HP')
        
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
        
    def test_client_fetch_messages(self):
        client = ChatClient('User 1')
        client.connection = unittest.mock.Mock()
        client.connection.get_messages.return_value = ['message1', 'message2']
        starting_messages = client.fetch_messages()
        client.connection.get_messages().append('message3')
        new_messages = client.fetch_messages()
        
        assert starting_messages == ['message1', 'message2']
        assert new_messages == ['message3']
        
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
        
    def test_exchange_with_server(self):
        with unittest.mock.patch(
            'multiprocessing.managers.listener_client', 
            new={
                'pickle': (
                    None, FakeServer(),
                ),
            },
        ):
            conn1 = Connection(('localhost', 9090))
            conn2 = Connection(('localhost', 9090))
            
            conn1.broadcast('connected message')
            assert conn2.get_messages()[-1] == 'connected message'
        
if __name__ == '__main__':
    unittest.main()