#! /usr/bin/env python3

import time 
import os 

def show_zone_info():
    print('TZ -> ', os.environ.get('TZ', '(not set)'))
    print('Tzname -> ', time.tzname)
    print(f'Zone -> {time.timezone} ({time.timezone / 3600})')
    print('DST -> ', time.daylight)
    print('Time -> ', time.ctime())
    print()
    
print('Default -> ')
show_zone_info()

ZONES = [
    'GMT', 
    'Europe/Moscow',
]

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ' -> ')
    show_zone_info()