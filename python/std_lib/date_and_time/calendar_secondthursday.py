#! /usr/bin/env python3 

import calendar
import sys 

year = int(sys.argv[1])

# show every month
for month in range(1, 13):
    # find date for every day of week with this month corelation
    cal = calendar.monthcalendar(year, month)
    first_week = cal[0]
    second_week = cal[1]
    thisrd_week = cal[2]
    
    # if first week include thursday -> second thursday in second week
    # else second thursday must be include in third week
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = thisrd_week[calendar.THURSDAY]
        
    print(f'{calendar.month_abbr[month]:>3} -> {meeting_date:>2}')