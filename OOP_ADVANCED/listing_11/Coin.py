#! /usr/bin/env python3 

import random

class Coin:
    """
    >>> import random 
    >>> my_coin = Coin()
    >>> print(my_coin.get_sideup())
    Igle
    """

    def __init__(self) -> None:
        self.__sideup = 'Igle'
    
    def toss(self) -> None:
        if random.randint(0, 1) == 0:
            self.__sideup = 'Igle'
        else:
            self.__sideup = 'NoIgle'

    def get_sideup(self) -> str:
        return self.__sideup

if __name__ == '__main__':
    import doctest
    doctest.testmod()