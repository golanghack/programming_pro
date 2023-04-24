#! /usr/bin/env python3 

from urllib.parse import quote, quote_plus, urlencode

url = 'http://localhost:8080/neo/'
print('urlencode() -> ', urlencode({'url': url}))
print('quote() -> ', quote(url))
print('quote_plus() -> ', quote_plus(url))