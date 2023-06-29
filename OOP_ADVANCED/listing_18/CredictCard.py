#! /usr/bin/env python3

class CreditCard:
    """A consumet credit card"""

    def __init__(self, customer: str, bank: str, account: str, limit: float) -> None:
        """Create a new credit card instance.

        The initial balance is zero.
        
        customer the name of the customer(e.g., 'John Dow')
        bank the name of the bank(e.g., 'Bank of America')
        account the account identifier(e.g., '4543 3456 5454 4345')
        limit the credit limit(measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self) -> str:
        """Return name of the customer"""

        return self._customer

    def get_bank(self) -> str:
        """Return the bank`s name""" 

        return self._bank

    def get_account(self) -> str:
        """Return the card identifying number (typically stored as a string).""" 

        return self._account

    def get_limit(self) -> float:
        """Return current credit limit.""" 

        return self._limit

    def get_balance(self) -> float:
        """Return current balance."""

        return self._balance

    def charge(self, price: float) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was prossed; False if charge was denied.
        """ 

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: float) -> None:
        """Process customer payment that reduces balance."""

        self._balance -= amount
