#! /usr/bin/env python3 

import datetime

one_day = datetime.timedelta(days=1)

print('1 day -> ', one_day)
print('5 days -> ', one_day * 5)
print('1.5 days -> ', one_day * 1.5)
print('1/4 day -> ', one_day / 4)

# one hour from day 
work_day = datetime.timedelta(hours=7)
meeting_lenght = datetime.timedelta(hours=1)
print('meeting per day -> ', work_day / meeting_lenght)