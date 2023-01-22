#! /usr/bin/env python3 

import re 

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

candidates = [
    u'first.last@example.com',
    u'first.last_category@gmail.com',
    u'valid-address@mail.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    print(f'{candidate:<30} {"matches" if match else "No match"}')