#! /usr/bin/env python3 

import unittest
from .Auth import Authentication

class TestAuth(unittest.TestCase):
    
    def test_login(self):
        auth = Authentication()
        auth.USERS = [
            {
                'username': 'testuser', 
                'password': 'testpass',
            },
        ]
        responce = auth.login('testuser', 'testpass')
        
        assert responce == {
            'username': 'testuser', 
            'password': 'testpass',
        }
        
        