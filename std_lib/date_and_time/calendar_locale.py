#! /usr/bin/env python3

import calendar

cal = calendar.LocaleTextCalendar(locale='ru_Ru.UTF-8')
cal.prmonth(2023, 1)

print()

cal = calendar.LocaleTextCalendar(locale='en_US.UTF-8')
cal.prmonth(2023, 1)