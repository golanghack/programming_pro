#! /usr/bin/env python3

import re 

address = re.compile(
    """ 
    ^ 
    # name include letters and symbols '.'
    # and short options initilas 
    (?P<name>
    ([\w.]+\s+)*[\w.]+
    )?
    \s*
    # email addresses must be include in '<>' only when found name
    (?(name)
    # reminder included in '<>' because have a name
    (?P<brackets>(?=(<.*>$)))
    |
    # reminder dont include '<>' dont have name
    (?=([^<].*[^>]$))
    )
    # to find '<>' only if before testing found '<>'
    (?(brackets)<|\s*)
    # email -> username@domain.tld
    (?P<email>
    [\w\d.+-]+ # username 
    @
    ([\w\d.]+\.)+ # prefix name of domain
    (com|org|edu) # up level limit
    )
    # find '<>' only if before testing found '<>'
    (?(brackets)>|\s*)
    $
    """,
    re.VERBOSE
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
        print('<-- Match name --> ', match.groupdict()['name'])
        print('<-- Match email--> ', match.groupdict()['email'])
    else:
        print('No match')