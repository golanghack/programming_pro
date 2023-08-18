#! /usr/bin/env python3 

from statistics import * 

data = [10, 20, 30, 40]

print(f'1 -> {median_grouped(data, interval=1):0.2f}')
print(f'2 -> {median_grouped(data, interval=2):0.2f}')
print(f'3 -> {median_grouped(data, interval=3):0.2f}')