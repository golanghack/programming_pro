#! /usr/bin/env python3 

import imaplib
from imaplib_connect import open_connecttion

with open_connecttion() as conn:
    typ, data = conn.list()
    print('Response code -> ', typ)
    print('Response -> ')
    print(data)