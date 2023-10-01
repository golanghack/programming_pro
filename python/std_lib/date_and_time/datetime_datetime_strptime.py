#! /usr/bin/env python3 

import datetime

format_ = '%a %b %d %H:%M:%S %Y'

today = datetime.datetime.today()
print('ISO -> ', today)

str_time = today.strftime(format_)
print('strftime -> ', str_time)

datetime_str = datetime.datetime.strptime(str_time, format_)
print('strptime -> ', datetime_str.strftime(format_))