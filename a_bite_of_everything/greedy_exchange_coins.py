#! /usr/bin/env python3 

def greedy(coin_values: list, change: int) -> int:
    """Return coins."""
    
    coin_values.sort()
    coin_values.reverse()
    
    num_coins = 0
    
    for coin in coin_values:
        num_coins += change // coin
        change = change % coin 
    return num_coins