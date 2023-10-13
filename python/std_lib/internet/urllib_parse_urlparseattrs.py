#! /usr/bin/env python3

from urllib.parse import urlparse

url = 'https://nasa.gov'
parsed = urlparse(url)
print('scheme -> ', parsed.scheme)
print('netloc -> ', parsed.netloc)
print('path -> ', parsed.path)
print('params -> ', parsed.params)
print('query -> ', parsed.query)
print('fragment -> ', parsed.fragment)
print('username -> ', parsed.username)
print('password -> ', parsed.password)
print('hostname -> ', parsed.hostname)
print('port     -> ', parsed.port)