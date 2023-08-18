#! /usr/bin/env python3 

class Account():
    """Account"""

    def __init__(self, name: str, balance: float, password: str) -> None:
        self.name = name 
        self.balance = float(balance)
        self.password = password

    def deposit(self, amount_deposit, password):
        if password != self.password or amount_deposit < 0:
            print('Sorry, uncorrect password or amount deposit negative')
            return None
        self.balance = self.balance + amount_deposit
        return self.balance

    def with_draw(self, amount_draw, password):
        if password != self.password or amount_draw < 0:
            print('Uncorrect password or negative withdraw.')
            return None
        if amount_draw > self.balance:
            print('You cannt withdraw more than you have in your account')
            return None
        self.balance = self.balance - amount_draw
        return self.balance

    def get_balance(self, password):
        if password != self.password:
            return None
        return self.balance

    def show(self):
        print(f'Name -> {self.name}')
        print(f'Balance -> {self.balance}')
        print(f'Password -> ', self.password)
        print()

