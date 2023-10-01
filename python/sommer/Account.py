#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import pickle

class SaveError(Exception): pass
class LoadError(Exception): pass

class Transaction:
    
    def __init__(self, 
                 amount: float, 
                 date: str, 
                 currency: str='USD',
                 usd_conversion_rate: int=1, 
                 description: str= None) -> None:
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (100, 'USD', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "EUR", 1.53)
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (250, 'EUR', 1.53, 382.5)
        """
        
        self.__amount = amount
        self.__date = date
        self.__description = description
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        
    @property
    def amount(self) -> float:
        return self.__amount
    
    @property
    def date(self) -> str:
        return self.__date
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def currency(self) -> str:
        return self.__currency
    
    @property
    def usd_conversion_rate(self) -> float:
        return self.__usd_conversion_rate
    
    @property
    def usd(self) -> float:
        return self.__amount * self.__usd_conversion_rate
    
class Account:
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Golanghack")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Golanghack')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2018-11-14"))
    >>> account.apply(Transaction(150, "2018-12-09"))
    >>> account.apply(Transaction(-95, "2019-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2018-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Golanghack")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """
    
    def __init__(self, number: int, name: str) -> None:
        """Creates a new account with the given number and name

        The number is used as the account's filename.
        """
        
        self.__number: int = number
        self.__name: str = name
        self.__transactions: list = []
        
        
    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> str:
        assert len(name) > 3, 'account name must be at least 4 characters'
        self.__name = name
        
    def __len__(self) -> int:
        return len(self.__transactions)
    
    def apply(self, trans) -> list:
        self.__transactions.append(trans)
        
    @property
    def balance(self) -> float:
        total: float = 0.0
        for trans in self.__transactions:
            total += trans.usd
        return total
    
    @property
    def all_usd(self) -> bool:
        for trans in self.__transactions:
            if trans.currency != 'USD':
                return False
        return True
    
    def save(self) -> None:
        fh = None
        try:
            data: list = [self.number, self.name, self.__transactions]
            fh = open(self.number + '.acc', 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
                
    def load(self) -> None:
        """Loads the account's data from file number.acc

        All previous data is lost.
        """
        
        fh = None
        try:
            fh = open(self.number + '.acc', 'rb')
            data = pickle.load(fh)
            assert self.number == data[0], 'account number doesn`t match'
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
        
        
        
        
        