#! /usr/bin/env python3 

from http import cookies
import datetime

def show_cookie(my_cookies):
    print(my_cookies)
    for key, morsel in my_cookies.items():
        print()
        print(f'key -> {morsel.key}')
        print(f'value -> {morsel.value}')
        print(f'coded_value -> {morsel.coded_value}')
        for name in morsel.keys():
            if morsel[name]:
                print(f'  {name} -> {morsel[name]}')

my_cookies = cookies.SimpleCookie()

my_cookies['encoded_value_cookie'] = '"cookie, value;"'
my_cookies['encoded_value_cookie']['comment'] = 'Has escaped punctuation'

# parts
my_cookies['restricted_cookie'] = 'cookie_value'
my_cookies['restricted_cookie']['path'] = '/sub/path'
my_cookies['restricted_cookie']['domain'] = 'nasa.gov'
my_cookies['restricted_cookie']['secure'] = True 

# 5 minut age 
my_cookies['with_max_age'] = 'expires in 5 minutes'
my_cookies['with_max_age']['max-age'] = 300

# point age
my_cookies['expires_at_time'] = 'cookie_value'
time_to_live = datetime.timedelta(hours=1)
expires = (datetime.datetime(2023, 5, 14, 18, 28, 14) + time_to_live)

# format -> Wdy, DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a, %d %b %Y %H:%M:%S')
my_cookies['expires_at_time']['expires'] = expires_at_time

show_cookie(my_cookies)