#! /usr/bin/env python3 

from urllib.parse import urlunparse, urlparse

original = 'https://nasa.gov'
print('original -> ', original)
parsed = urlparse(original)
print('parsed -> ', parsed, type(parsed))
t = parsed[:]
print('Tuple -> ', t, type(t))
print('new -> ', urlunparse(t))