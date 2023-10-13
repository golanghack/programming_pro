#! /usr/bin/env python3 

import imaplib_connect

with imaplib_connect.open_connecttion() as conn:
    typ, data = conn.select('Does-Not-Exist')
    print(typ, data)
    