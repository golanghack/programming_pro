#! /usr/bin/env python3 

import re 

address = re.compile(
    """ 
    # Email -> username@domain.tld
    [\w\d.+-]+ # username
    # ignored address noreply 
    (?<!noreply)
    @
    ([\w\d.]+\.)+ # prefix name of domain
    (com|org|edu) # up level border
    $
    """, 
    re.VERBOSE
)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
]

for candidate in candidates:
    print('Candidate -> ', candidate)
    match = address.search(candidate)
    if match:
        print('Match -> ', candidate[match.start():match.end()])
    else:
        print('No match')