#! /usr/bin/env python3 

from urllib.parse import parse_qsl, parse_qs

encoded = 'foo=foo1&foo2'

print('parse_qs -> ', parse_qs(encoded))
print('parse_qls -> ', parse_qsl(encoded))