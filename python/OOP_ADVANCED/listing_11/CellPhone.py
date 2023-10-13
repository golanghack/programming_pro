#! /usr/bin/env python3 

class CellPhone:
    """ 
    >>> man = 'Sams'
    >>> models = 'Sam'
    >>> retail = 100.0
    >>> phone = CellPhone(man, models, retail)
    >>> print(phone.get_manufact())
    Sams
    >>> print(phone.get_model())
    Sam
    >>> print(phone.get_price())
    100.0
    """ 

    def __init__(self, mark: str, mod: str, price: float) -> None:
        self.__manufact = mark
        self.__model = mod
        self.__retail_price = price

    def set_manufact(self, mark):
        self.__manufact = mark

    def set_model(self, mod):
        self.__model = mod 

    def set_retail_price(self, price):
        self.__retail_price = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__retail_price

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()