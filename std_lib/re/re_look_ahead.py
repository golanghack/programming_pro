#! /usr/bin/env python3 

import re 

address = re.compile(
    """ 
    # Name include letters and symbols of '.'
    #  and in shortcat options 
    ((?P<name>
    ([\w.,]+\s+)*[\w.,\+
    )
    \s+
    ) # Name dont must have
    # LOOK FOR ->
    # Addresses of email inlcude '<>" only if both '<>' or not in '<>'
    (?= (<.*>$) # have '<>'
    |
    ([^<].*[^>]$) # dont have '<>'
    )
    <? # dont must have
    # email -> username@domain.tld
    (?P<email>
    [\w\d.+-]+ # username
    @
    ([\w\d.]+\.)+ # prefix name of domain
    (com|org|edu) # up level border
    )
    >? # dont must have '<>'
    """, re.VERBOSE
)

candidates = [
    u'first.last@example.com',
    u'first.last_category@gmail.com',
    u'valid-address@mail.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    print('Candidate -> ', candidate)
    match = address.search(candidate)
    if match:
        print('   Name -> ', match.groupdict()['name'])
        print('   Email -> ', match.groupdict()['email'])
    else:
        print('No match')