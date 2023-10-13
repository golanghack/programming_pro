#! /usr/bin/env python3 

import datetime 

today = datetime.datetime.today()

print('ISO -> ', today)
print('format () -> {:%a %b %d %H:%M:%S %Y}'.format(today))