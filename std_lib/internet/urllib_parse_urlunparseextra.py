#! /usr/bin/env python3 

from urllib.parse import urlparse, urlunparse

original = 'https://nasa.gov'
print('original -> ', original)
parsed = urlparse(original)
print('parsed -> ', parsed, type(parsed))
t = parsed[:]
print('Tuple -> ', type(t), t)
print('new -> ', urlunparse(t))