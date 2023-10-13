#! /usr/bin/env python3 

from urllib.parse import urlencode

query_args = {
    'q': 'query string', 
    'foo': 'bar',
}

encoded_args = urlencode(query_args)
print('Encoded -> ', encoded_args)
