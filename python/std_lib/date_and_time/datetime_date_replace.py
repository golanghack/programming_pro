#! /usr/bin/env python3 

import datetime 

data_one = datetime.date(2023, 2, 9)
print('date_one -> ', data_one.ctime())

date_two = data_one.replace(year=2024)
print('date_two -> ', date_two.ctime())