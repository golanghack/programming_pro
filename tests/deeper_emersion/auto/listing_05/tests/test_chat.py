#! /usr/bin/env python3

import unittest

class TestChatMultiUser(unittest.TestCase):
    
    def test_many_users(self):
        with new_chat_server() as serv:
            first_user = ChatClient('J Doe')
            
            for uid in range(5):
                more_user = ChatClient(f'User {uid}')
                more_user.send_message('Hello')
                
            messages = first_user.fetch_messages()
            assert len(messages) == 5
            
    def test_multiple_readers(self):
        with new_chat_server() as serv:
            user_1 = ChatClient('J Doe')
            user_2 = ChatClient('User 2')
            user_3 = ChatClient('User 3')
            
            user_1.send_message('Hi all')
            user_2.send_message('Hello World')
            user_3.send_message('Hi')
            
            user_1_messages = user_1.fetch_messages()
            user_2_messages = user_2.fetch_messages()
            
            self.assertEqual(user_1_messages, user_2_messages)
            
unittest.main()