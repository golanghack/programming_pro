#! /usr/bin/env python3 

import unittest

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
        
if __name__ == '__main__':
    unittest.main()