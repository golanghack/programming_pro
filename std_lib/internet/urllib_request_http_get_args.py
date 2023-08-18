#! /usr/bin/env python3 

from urllib import parse, request

query_args = {'q': 'query_string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args)
print('Encoded -> ', encoded_args)

url = 'https://example.com/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))