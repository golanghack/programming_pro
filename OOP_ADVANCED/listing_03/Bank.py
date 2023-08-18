#! /usr/bin/env python3 

from Account import Account 


class Bank():

    def __init__(self, hours: int, address: str, phone: int) -> None:
        self.account_dict = {}
        self.next_account_number = 0 
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input('What is your account number? -> ')
        try:
            account_number = int(account_number)
        except ValueError:
            print('The account number must be an integer')
        if account_number not in self.account_dict:
            print('The is no account '.join(account_number))
        return account_number

    def get_user_account(self):
        account_number = self.ask_for_valid_account_number()
        new_account = self.account_dict[account_number]
        self.ask_for_valid_password(new_account)
        return new_account

    def ask_for_valid_password(self, new_account):
        password = input('Please enter your password -> ')
        new_account.check_password(password)

    def create_account(self, name, starting_amount, password):
        new_account = Account(name, starting_amount, password)
        new_account_number = self.next_account_number
        self.account_dict[new_account_number] = new_account
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print('<-- Open Account -->')
        user_name = input('What is your name? ')
        user_starting_amount = input('How much money to start your account? ')
        user_password = input('What password would you like to use for this account? ')
        user_account_number = self.create_account(user_name, 
                                   user_starting_amount, 
                                   user_password)
        print('Your new account number is -> ', user_account_number)

    def close_account(self):
        print('<-- Close Account -->')
        user_account_number = self.ask_for_valid_account_number()
        new_account = self.account_dict[user_account_number]
        self.ask_for_valid_password(new_account)
        balance = new_account.get_balance()
        print(f'You had -> {balance}, in your account, which is being returned to you.')
        del self.account_dict[user_account_number]
        print('Your account is now closed')

    def balance(self):
        print('<-- Get Balance -->')
        new_account = self.get_user_account()
        balance = new_account.get_balance()
        print(f'Your balance -> {balance}')

    def deposit(self):
        print('<-- Deposit -->')
        new_account = self.get_user_account()
        deposit_amount = input('Please enter amount to deposit -> ')
        balance = new_account.deposit(deposit_amount)
        print(f'Deposited -> {deposit_amount}')
        print(f'Your new balance is -> {balance}')

    def with_draw(self):
        print('<-- Withdraw -->')
        new_account = self.get_user_account()
        user_amount = input('Please enetr the amount to withdraw -> ')
        balance = new_account.with_draw(user_amount)
        print('With drew', user_amount)
        print('Your new balance -> ', balance)

    def gew_info(self):
        print(f'Hours -> {self.hours}')
        print(f'Address -> {self.address}')
        print(f'Phone -> {self.phone}')
        print(f'We currently have -> {len(self.account_dict)}, account(s) open.')

    #  for admin only
    def show(self):
        print('<-- Show -->')
        print('This would typically require an admin pass')
        for user_account_number in self.account_dict.items():
            new_account = self.account_dict[user_account_number]
            print(f'Account -> {user_account_number}')
            new_account.show()
            print()    
