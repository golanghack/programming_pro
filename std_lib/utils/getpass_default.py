#! /usr/bin/env python3 

import getpass

try:
    password = getpass.getpass()
except Exception as err:
    print(f'Error  {err}')
else:
    print(f'Entered -> {password}')