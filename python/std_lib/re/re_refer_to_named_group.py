#! /usr/bin/env python3

import re 

address = re.compile(
    """ 
    #initial usual form
    (?P<first_name>\w+)
    \s+
    (([\w.]+)\s+)? # dont must have initials 
    (?P<last_name>\w+)
    \s+
    <
    # email -> name.lastname@domain.tld
    (?P<email>
    (?P=first_name)
    \.
    (?P=last_name)
    @
    ([\w\d.]+\.)+ # prefix domain up level
    (com|org|edu) # up level limit 
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
        print('<-- Match name --> ', match.groupdict()['first_name'], end=' ')
        print(match.groupdict()['last_name'])
        print('<-- Match email--> ', match.groupdict()['email'])
    else:
        print('No match')