#! /usr/bin/env python3 

"""  
Problem 

Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
""" 
import random

record = '0123456789012345678901234567890123456789012345678901234567890'

SHARES = slice(20, 22)
PRICES = slice(40, 42)

full_cost = int(record[SHARES]) * float(record[PRICES])

