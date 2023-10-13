#! /usr/bin/env python3 

import unittest
import unittest.mock
from chat.client import ChatClient
from fakeserver import FakeServer

class TestChatMessageExchange(unittest.TestCase):
    
    def setUp(self) -> None:
        self.fakeserver = unittest.mock.patch('multiprocessing.managers.listener_client',
                                              new={'pickle': (None, FakeServer())})
        self.fakeserver.start()
        
        
    def tearDown(self) -> None:
        self.fakeserver.stop()
        
    def test_exchange_with_server(self):
        c1 = ChatClient('User 1')
        c2 = ChatClient('User 2')
        
        c1.send_message('connected message')
        
        assert c2.fetch_messages()[-1] == 'User 1: connected message'
        
    def test_many_users(self):
        first_user = ChatClient('JD')
        
        for uid in range(5):
            more_user = ChatClient(f'User {uid}')
            more_user.send_message('Hi')
        
        messages = first_user.fetch_messages()
        assert len(messages) == 5
        
    def test_multiple_readers(self):
        user_1 = ChatClient('JD')
        user_2 = ChatClient('User 2')
        user_3 = ChatClient('User 3')
        
        user_1.send_message('Hi all')
        user_2.send_message('Hello World')
        user_3.send_message('Hi')
        
        user_1_messages = user_1.fetch_messages()
        user_2_messages = user_2.fetch_messages()
        
        self.assertEqual(user_1_messages, user_2_messages)
        
unittest.main()