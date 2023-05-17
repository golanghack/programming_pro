#! /usr/bin/env python3 

import xmlrpc.client
import datetime
import pprint


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

arg = []

for i in range(3):
    dict_types = {}
    dict_types.update(data)
    dict_types['integer']= i 
    arg.append(dict_types)

print('Before -> ')
pprint.pprint(arg, width=40)

print('\nAfter ->')
pprint.pprint(server.show_types(arg)[-1], width=40)