#! /usr/bin/env python3 

import unittest
from ChatClient import ChatClient

class TestChatClient(unittest.TestCase):
    
    def test_nickname(self):
        client = ChatClient('User 1')
        
        assert client.nickname == 'User 1'
        
    def test_semd_message(self):
        client = ChatClient('User 1')
        sent_message = client.send_message('Hi')
        
        assert sent_message == 'User 1: Hi'
        
        