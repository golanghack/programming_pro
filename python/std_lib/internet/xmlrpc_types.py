#! /usr/bin/env python3 

import xmlrpc.client
import datetime

server = xmlrpc.client.ServerProxy('http://localhost:9000')

data = [
    ('boolean', True),
    ('integer', 1),
    ('float', 2.5),
    ('string', 'some text'),
    ('datetime', datetime.datetime.now()),
    ('array', ['a', 'list']),
    ('array', ('a', 'tuple')),
    ('structure', {'a': 'dictonary'}),
]

for type_value, value in data:
    as_string, type_name, value = server.show_type(value)

    print(f'{type_value:<12} -> {as_string}')
    print(f'{"":12} -> {type_name}')
    print(f'{"":12} -> {value}')