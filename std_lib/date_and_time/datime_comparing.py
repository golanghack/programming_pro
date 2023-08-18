#! /usr/bin/env python3 

import datetime 
import time

print('Times -> ')
time_one = datetime.time(12, 55, 0)
print('time_one ->', time_one)

time_two = datetime.time(13, 5, 0)
print('time_two -> ', time_two)

print('time_one < time_two', time_one < time_two)
print()

print('Dates -> ')
date_one = datetime.date.today()
print('date_one -> ', date_one)

date_two = datetime.date.today() + datetime.timedelta(days=1)

print('date_two -> ', date_two)
print('date_one > date_two -> ', date_one > date_two)