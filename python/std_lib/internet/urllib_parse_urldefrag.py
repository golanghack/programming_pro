#! /usr/bin/env python3 

from urllib.parse import urldefrag

original = 'https://nasa.gov'
print('original -> ', original)
d = urldefrag(original)
print('url -> ', d.url)
print('fragment -> ', d.fragment)