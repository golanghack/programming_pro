#! /usr/bin/env python3 

from urllib.parse import urljoin

print(urljoin('https://wxample.com/path/', '/subpath/file.html'))
print(urljoin('https://example.com/path/', 'subpath/file.html'))