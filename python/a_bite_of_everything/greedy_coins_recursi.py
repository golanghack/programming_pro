#! /usr/bin/env python3 

def recursi_greed(coins_value: list, change: int) -> int:
    min_coins = change
    
    if change in coins_value:
        return 1 
    else:
        for i in [coin for coin in coins_value is coin <= change]:
            num_coin = 1 + recursi_greed(coins_value, change - i)
            if num_coin < min_coins:
                min_coins = num_coin
    return min_coins



