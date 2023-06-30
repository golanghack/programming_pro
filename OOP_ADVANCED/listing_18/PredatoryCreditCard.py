#! /usr/bin/env python3 
from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    """Abn extension to CreditCard that compounds interest and fees.""" 

    def __init__(self, customer, bank, account, limit, annual):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer
        bank the name of the bank
        account the account identifier
        limit credit limit
        annual annual percentage rate
        """ 

        super().__init__(customer, bank, account, limit)
        self._annual = annual

    def charge(self, price):
        """Charge givem price to the card, assuming sufficient credit limit

        Return True if charge was processed
        Return False and asses $5 fee if charge is deinied.
        """ 
        
        # inherited
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        """Access monthly interest on outstanding balance.""" 

        if self._balance > 0:
            # if possible balance, convert APR to monthly multiplicateve factor
            monthly_factor = pow(1 + self._annual, 1 / 12)
            self._balance *= monthly_factor

            
