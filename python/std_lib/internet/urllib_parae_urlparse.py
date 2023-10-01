#! /usr/bin/env python3 

from urllib.parse import urlparse

url = 'https://nasa.gov'

parsed = urlparse(url)
print(parsed)
