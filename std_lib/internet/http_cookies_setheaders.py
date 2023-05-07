#! /usr/bin/env python3 

from http import cookies 

my_cookies = cookies.SimpleCookie()
my_cookies['mycookie'] = 'cookie_value'
print(f'my cookies -> {my_cookies}')