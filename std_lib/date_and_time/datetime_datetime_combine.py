#! /usr/bin/env python3 

import datetime

date_time = datetime.time(1, 2, 3)
print('date_time -> ', date_time)

date_today = datetime.date.today()
print('date_today -> ', date_today)

date_combine = datetime.datetime.combine(date_today, date_time)
print('date_combine -> ', date_combine)