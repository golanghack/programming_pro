#! /usr/bin/env python3 

import time

def show_struct(s):
    print('tm_year -> ', s.tm_year)
    print('tm_mon -> ', s.tm_mon)
    print('tm_mday -> ', s.tm_mday)
    print('tm_hour -> ', s.tm_hour)
    print('tm_min -> ', s.tm_min)
    print('tm_sec -> ', s.tm_sec)
    print('tm_wday -> ', s.tm_wday)
    print('tm_yday -> ', s.tm_yday)
    print('tm_isdst -> ', s.tm_isdst)
    
now = time.ctime(1675961640.3433156)
print('Now -> ', now)

parsed = time.strptime(now)
print('\nParsed ->')
show_struct(parsed)

print('\nFormatted -> ', time.strftime('%a %b %d %H:%M:S %Y', parsed))