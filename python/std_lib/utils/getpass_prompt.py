#! /usr/bin/env python3 

import getpass

password = getpass.getpass(prompt='Enter password')
if password.lower() == 'password':
    print('Ok')
else:
    print('Bad')