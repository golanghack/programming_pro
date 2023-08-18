#! /usr/bin/env python3 

import re 

address = re.compile(
    """ 
    [\w\d.+-]+ # username
    @
    ([\w\d.]+\.)+ # Prefix name of domen
    (com|org|edu) # TODO -> support domens another domens up level
    """, 
    re.VERBOSE
)

candidates = [
    u'first.last@example.com',
    u'first.last_category@gmail.com',
    u'valid-address@mail.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    print(f'{candidate:<30}  {"Matches" if match else "No match"}')