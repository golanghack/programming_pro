#! /usr/bin/env python3 

from urllib.parse import urljoin

print(urljoin('https:/example.com/path/file.html', 'anyfile.html'))

print(urljoin('https://example.com/path/file.html', '../anyfile.html'))

