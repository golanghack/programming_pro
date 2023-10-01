#! /usr/bin/env python3 


from statistics import * 

data = [1, 2, 32, 5, 10, 12, 17]

print(f'median ->  {median(data):0.2f}')
print(f'low -> {median_low(data):0.2f}')
print(f'hight -> {median_high(data):0.2f}')
