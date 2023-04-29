#! /usr/bin/env python3 

account_name = 'Ben'
account_balance = 300
account_password = 'soup'

while True:
    print()
    print('Press b to the balance')
    print('Press d to the dipasit')
    print('Press w to the withdrawal')
    print('Press s to the sho account')
    print('Press q to quit')

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
