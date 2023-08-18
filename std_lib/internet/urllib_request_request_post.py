#! /usr/bin/env python3 

from urllib import parse, request

query_args  = {'q': 'query string', 'foo': 'bar',}

req = request.Request(url='http://localhost:8080/', 
                        data=parse.urlencode(query_args).encode('utf-8'),)

print('Request method -> ', req.get_method())

req.add_header('User-agent', 'Nasa -> (https://nasa.gov/)',)
print()

print('Out data -> ')
print(req.data)

print()
print('Server response -> ')
print(request.urlopen(req).read().decode('utf-8'))
