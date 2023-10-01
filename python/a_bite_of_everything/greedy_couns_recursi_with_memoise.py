#! /usr/bin/env python3 

def memoise(coins_value: list, change: int, now_result: list) -> int:
    min_coins = change
    
    if change in coins_value:
        now_result[change] = 1
        return 1 
    elif change in now_result:
        return now_result[change]
    else:
        for i in [coin for coin in coins_value if coin <= change]:
            num_coins = 1 + memoise(coins_value, change - i, now_result)
            if num_coins < min_coins:
                min_coins = num_coins
                now_result[change] = min_coins
    return min_coins

