#! /usr/bin/env python3 

import unittest
from Account import Account

class TestAccount(unittest.TestCase):
    
    def test_account_object_can_be_created(self):
        account = Account()
        
if __name__ == '__main__':
    unittest.main()