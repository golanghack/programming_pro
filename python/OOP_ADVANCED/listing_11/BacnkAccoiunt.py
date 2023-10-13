#! /usr/bin/env python3 

class BankAccount:

    def __init__(self, input_balance: float) -> None:
        self.__balance = input_balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error!')

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self):
        return str(self.__balance)


if __name__ == '__main__':
    import doctest
    doctest.testmod(

    )