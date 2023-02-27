#! /usr/bin/env python3 

import unittest
from ChatClient import ChatClient

class TestChatClient(unittest.TestCase):
    
    def test_nickname(self):
        client = ChatClient('User 1')
        
        assert client.nickname == 'User 1'