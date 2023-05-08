#! /usr/bin/env python3 

from http import cookies
import textwrap

my_cookie = cookies.SimpleCookie()
my_cookie['mycookie'] = 'cookie value'
my_cookie['another_cookie'] = 'second value'
js_text = my_cookie.js_output()
print(textwrap.dedent(js_text).lstrip())