#! /usr/bin/env python3 

"""  
Problem 

You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.
"""

currency_prices = {
    'DOL': 100.00, 
    'EUR': 198.00, 
    'FRA': 44.00,
    'YEN': 10.76,
}

min_price = min(zip(currency_prices.values(), currency_prices.keys()))
max_price = max(zip(currency_prices.values(), currency_prices.keys()))
sorted_prices = sorted(zip(currency_prices.values(), currency_prices.keys()))



