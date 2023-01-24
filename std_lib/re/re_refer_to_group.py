#! /usr/bin/env python3 

import re

address = re.compile(
    r""" 
    (\w+) # name
    \s+
    (([\w.]+)\s+)? #dont must have initials
    (\w+) # surname
    \s+
    <
    #email -> name.surname@domain.tld
    (?P<email>
    \1 # name
    \.
    \4 # surname
    @
    ([\w\d.]+\.)+ # prefix name of domain
    (com|org|edu) # up level border 
    )
    >
    """,
    re.VERBOSE | re.IGNORECASE
)

candidates = [
    u'First Last first.last@example.com' ,
    u'Different Name first.last+category@gmail.com',
    u'First Middle Name valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
]

for candidate in candidates:
    print('Candidate -> ', candidate)
    match = address.search(candidate)
    if match:
        print('<-- Match name --> ', match.group(1), match.group(4))
        print('<-- Match email--> ', match.group(5))
    else:
        print('No match')