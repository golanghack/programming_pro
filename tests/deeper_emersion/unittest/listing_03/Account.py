#! /usr/bin/env python3 

class Account(object):
    
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

