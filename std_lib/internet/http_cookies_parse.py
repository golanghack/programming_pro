#! /usr/bin/env python3 

from  http import cookies

HTTP_COOKIE = '; '.join([r'integer=5', r'with_quotes="SEND -> \"Hello\""',])

print('From constructor -> ')
my_cookie = cookies.SimpleCookie(HTTP_COOKIE)
print(my_cookie)

print()
print('From load()-> ')
my_cookie = cookies.SimpleCookie()
my_cookie.load(HTTP_COOKIE)
print(my_cookie)