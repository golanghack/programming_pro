#! /usr/bin/env python3 

import calendar

cal = calendar.TextCalendar(calendar.MONDAY)
print(cal.formatyear(2023, 2, 1, 1, 3))