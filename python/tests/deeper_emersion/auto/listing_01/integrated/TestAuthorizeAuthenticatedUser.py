#! /usr/bin/env python3 

import unittest
from .Auth import Authentication
from .Auth import Authorization

class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [
        {
            'user':'testuser',
            'permissions': {'create'},
        },
        ]
        response = authz.can({'username': 'testuser'}, 'create')
        assert response is True

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
        
class TestAuthorizeAuthenticatedUser(unittest.TestCase):
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()
        auth.USERS = [
            {
                'username': 'testuser', 
                'password': 'testpass',
            },
        ]
        authz.PERMISSIONS = [
            {
                'user': 'testuser', 
                'permissions': {'create'},
            },
        ]
        u = auth.login('testuser', 'testpass')
        response = authz.can(u, 'create')
        assert response is True