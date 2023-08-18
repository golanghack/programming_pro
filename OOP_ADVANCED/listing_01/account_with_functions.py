#! /usr/bin/env python3 

account_name = ''
account_balance = 0 
account_password = ''

def new_account(name: str, balance: float, password: str):

    global account_name, account_balance, account_password 
    account_name = name
    account_balance = balance
    account_password = password

def show():
    
    global account_name, account_balance, account_password
    print(f'Name -> {account_name}')
    print(f'Balance -> {account_balance}')
    print(f'Password -> {account_password}')
    print()

def get_balance(password: str) -> float:
    global account_name, account_balance, account_password
    if password != account_password:
        print('Uncorrect password')
        return None
    return account_balance

def deposit(amount_deposit, password):
    global account_name, account_balance, account_password
    if amount_deposit < 0:
        print('You cannot deposit a negative amount')
        return None

    if password != account_password:
        print('Uncorrect passwor')
        return None

    account_balance = account_balance + amount_deposit
    return account_balance

def with_draw(amount_with_draw, password):
    global account_name, account_balance, account_password
    if amount_with_draw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if password != account_password:
        print('Uncorrect password for this account')
        return None
    
    if amount_with_draw > account_balance:
        print('You cannot withdraw more than you have in your asccount')
        return None

    account_balance = account_balance - amount_with_draw
    return account_balance

new_account('Ben', 400, '123')

while True:
    print()
    print('press b to get balance')
    print('press d for make deposit')
    print('press w to make a withdraw')
    print('press s to show account')
    print('q to quit')
    print()

     message = 'What do you want to do? '
    action = input(message)
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance ->')
        user_password = input('Enter password -> ')
        if user_password != account_password:
            print('Uncorrect password')
        else:
            print(f'Your balance -> {account_balance}')
    elif action == 'd':
        print('Deposit -> ')
        user_deposit_amount = input('Please enetr amount deposit -> ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password -> ')

        if user_deposit_amount < 0:
            print('You cannot deposit a negative amount')
        elif user_password != account_password:
            print('Uncorrect passwor')
        else:
            account_balance = account_balance + user_deposit_amount
            print('Your new balance is -> ', account_balance)

    elif action == 's':
        print('Show')
        print(f'Name -> {account_name}')
        print(f'Balance -> {account_balance}')
        print(f'Password -> {account_password}')
        print()
    
    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw -> ')
        user_with_draw_amount = input('please enetr the amount to withdraw -> ')
        user_with_draw_amount = int(user_with_draw_amount)
        user_password = input('Enter the password -> ')

        if user_with_draw_amount < 0:
            print('You cannot withdraw a negative amount')
        elif user_password != account_password:
            print('uncorrect password for this account')
        elif user_with_draw_amount > account_balance:
            print('you cannot withdraw more than you have in your account')
        else:
            account_balance = account_balance - user_with_draw_amount
            print('Your new balance is ', account_balance)

print('Done')
