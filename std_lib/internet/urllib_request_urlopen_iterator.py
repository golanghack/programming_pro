#! /usr/bin/env python3 

from urllib import request

response = request.urlopen('https://example.com')
for line in response:
    print(line.decode('utf-8').rstrip())