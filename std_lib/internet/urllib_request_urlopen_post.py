#! /usr/bin/env python3 

from urllib import parse, request

query_args = {'q': 'query_string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args).encode('utf-8')
url = 'https://example.com'

print(request.urlopen(url, encoded_args).read().decode('utf-8'))