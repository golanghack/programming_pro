#! /usr/bin/env python3 

import unittest
from Account import Account
from Bank import Bank

class BankTest(unittest.TestCase):
    
    def test_bank_is_initially_empty(self):
        bank = Bank()
        
        self.assertEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts), 0)
        
    def test_add_account(self):
        bank = Bank()
        
        account_1 = Account('001', 50)
        account_2 = Account('002', 100)
        
        bank.add_account(account_1)
        bank.add_account(account_2)
        
        self.assertEqual(len(bank.accounts), 2)
        
    def test_get_account_balance(self):
        bank = Bank()
        
        account_1 = Account('001', 50)
        bank.add_account(account_1)
        
        self.assertEqual(bank.get_account_balance('001'), 50)
        
if __name__ == '__main__':
    unittest.main()