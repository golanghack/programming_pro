#! /usr/bin/env python3 

from urllib.parse import urlparse

original = 'https://nasa.gov'
print('ORIG -> ', original)
parsed = urlparse(original)
print('PARSED -> ', parsed.geturl())