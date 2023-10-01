#! /usr/bin/env python3
from multiprocessing.managers import SyncManager
import unittest
from ChatClient import ChatClient

class TestChatAcceptance(unittest.TestCase):
    
    def test_message_exchange(self):
        user1 = ChatClient('John Doe')
        user2 = ChatClient('Harry Potter')
        
        user1.send_message('Hello')
        messages = user2.fetch_messages()
        
        assert messages == ['John Doe: Hello']
 
_messages = []
def _srv_get_messages():
    return _messages
class _ChatServerManager(SyncManager):
    pass
_ChatServerManager.register('get_messages', 
                            callable=_srv_get_messages, 
                            proxytype=ListProxy)

def new_chat_server():
    return _ChatServerManager(('', 9090), authkey=b'mychatsecret')

if __name__ == '__main__':
    unittest.main()