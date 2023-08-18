#! /usr/bin/env python3 

import unittest
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