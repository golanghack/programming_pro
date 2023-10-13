#! /usr/bin/env python3 

class Account():

    def __init__(self, name: str, 
                        balance: int, 
                        password: str) -> None:

        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amount_to_deposite: int, password: str) -> None:
        messages = ['Sorry, incorect password',
                    'You deposit a negative amount']
        if password != self.password:
            print(messages[0])
            return None
        if amount_to_deposite < 0:
            print(messages[1]) 
            return None
        self.balance = self.balance + amount_to_deposite
        return self.balance

    def withdraw(self, amount_to_withdraw: int, password: str) -> None:
        messages = [
            'Incorrect password for this account',
            'You cannot withdraw a negative amount',
            'You cannot withdraw more than you have in your account',
        ]
        if password != self.password:
            print(messages[0])
            return None
        if amount_to_withdraw < 0:
            print(messages[1])
            return None
        if amount_to_withdraw > self.balance:
            print(messages[2])
            return None
        self.balance = self.balance - amount_to_withdraw
        return self.balance

    def get_balamce(self, password: str) -> None|int:
        if password != self.password:
            print('Sorry, incorect password')
            return None
        return self.balance

    def show(self) -> None:
        print(f'Name -> {self.name}')
        print(f'Balance -> {self.balance}')
        print(f'Password -> {self.password}')
        print()