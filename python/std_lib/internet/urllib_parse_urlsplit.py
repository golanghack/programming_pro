#! /usr/bin/env python3 

from urllib.parse import urlsplit

url = 'https://nasa.gov'
parsed = urlsplit(url)

print(parsed)