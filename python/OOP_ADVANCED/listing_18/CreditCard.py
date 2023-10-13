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

if __name__ == '__main__':
    my_wallet = []
    my_wallet.append(CreditCard('One User', 'Bank one', '1111 1111 1111 1111', 1000))
    my_wallet.append(CreditCard('Two User', 'Bank Two', '2222 2222 2222 2222', 2000))
    my_wallet.append(CreditCard('Thre User', 'Bank Three', '3333 3333 3333 3333', 3000))

    for value in range(1, 17):
        my_wallet[0].charge(value)
        my_wallet[1].charge(2 * value)
        my_wallet[2].charge(3 * value)

    for custom in range(3):
        print(f'Customer -> {my_wallet[custom].get_customer()}')
        print(f'Bank -> {my_wallet[custom].get_bank()}')
        print(f'Account -> {my_wallet[custom].get_account()}')
        print(f'Limit -> {my_wallet[custom].get_limit()}')
        print(f'Balance -> {my_wallet[custom].get_balance()}')
        
        while my_wallet[custom].get_balance() > 100:
            my_wallet[custom].make_payment(100)
            print(f'New balance -> {my_wallet[custom].get_balance()}')
        print()
