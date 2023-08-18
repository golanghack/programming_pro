#! /usr/bin/env python3 

class Bank(object):
    def __init__(self):
        self.accounts = {}
        
    def add_account(self, account: str):
        self.accounts[account.account_number] = account.balance
        
    def get_account_balance(self, account_number: str):
        return self.accounts.get(account_number)