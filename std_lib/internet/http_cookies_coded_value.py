#! /usr/bin/env python3 

from http import cookies

my_cookies = cookies.SimpleCookie()
my_cookies['integer'] = 5
my_cookies['with_quotes'] = 'Send "Hello"'

for name in ['integer', 'with_quotes']:
    print(my_cookies[name].key)
    print(f'{my_cookies[name]}')
    print(f'value -> {my_cookies[name].value!r}')
    print(f'coded_value -> {my_cookies[name].coded_value!r}')