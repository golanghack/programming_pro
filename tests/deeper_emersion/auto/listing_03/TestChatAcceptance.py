#! /usr/bin/env python3

import unittest

class TestChatAcceptance(unittest.TestCase):
    
    def test_message_exchange(self):
        user1 = ChatClient('John Doe')
        user2 = ChatClient('Harry Potter')
        
        user1.send_message('Hello')
        messages = user2.fetch_messages()
        
        assert messages == ['John Doe: Hello']
        
if __name__ == '__main__':
    unittest.main()