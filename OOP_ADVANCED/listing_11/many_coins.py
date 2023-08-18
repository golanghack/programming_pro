#! /usr/bin/env python3 

from Coin import Coin

coin1 = Coin()
coin2 = Coin()
coin3 = Coin()

print(coin1.get_sideup())
print(coin2.get_sideup())
print(coin3.get_sideup())

coin1.toss()
coin2.toss()
coin3.toss()


print(coin1.get_sideup())
print(coin2.get_sideup())
print(coin3.get_sideup())